# seismic_app/views.py
from django.shortcuts import render
from .forms import DateRangeForm
import csv
from datetime import datetime, timedelta
import os
from django.conf import settings

def seismic_data_view(request):
    results = []
    error_message = ''
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            from_date_str = form.cleaned_data['from_date']
            to_date_str = form.cleaned_data['to_date']

            try:
                from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
                to_date = datetime.strptime(to_date_str, '%Y-%m-%d')

                if from_date > to_date:
                    error_message = 'From date must be earlier than To date.'
                else:
                    csv_file_path = os.path.join(settings.BASE_DIR,'space_apps_2024_seismic_detection', 'data', 'lunar','training', 'catalogs', 'apollo12_catalog_GradeA_final.csv')
                    with open(csv_file_path, 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            event_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f')
                            if from_date <= event_time <= to_date:
                                filename = row['filename']
                                max_velocity = get_max_velocity(filename,event_time)
                                results.append({
                                    'filename': filename,
                                    'event_time': event_time,
                                    'max_velocity': max_velocity,
                                })
            except ValueError:
                error_message = 'Invalid date format. Please use YYYY-MM-DD.'
    else:
        form = DateRangeForm()
    return render(request, 'seismic_app/seismic_data.html', {'form': form, 'results': results, 'error_message': error_message})


def binary_search_time(data, target_time, lower_bound=True):
    low, high = 0, len(data) - 1
    best_idx = None
    
    while low <= high:
        mid = (low + high) // 2
        mid_time = datetime.strptime(data[mid]['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f').replace(second=0, microsecond=0)
        
        if mid_time < target_time:
            low = mid + 1
        elif mid_time > target_time:
            high = mid - 1
        else:
            best_idx = mid
            if lower_bound:
                high = mid - 1  
            else:
                low = mid + 1  
    
    return best_idx

def get_max_velocity(filename, event_time):
    # Adjust the path to where your data files are located
    data_file_path = os.path.join(settings.BASE_DIR, 'space_apps_2024_seismic_detection', 'data', 'lunar', 'training', 'data', 'S12_GradeA', filename + '.csv')

    max_velocity = None

    try:
        with open(data_file_path, 'r') as datafile:
            reader = list(csv.DictReader(datafile))

        event_time_truncated = event_time.replace(second=0, microsecond=0)

        time_lower_bound = event_time_truncated - timedelta(minutes=1)
        time_upper_bound = event_time_truncated + timedelta(minutes=1)

        start_idx = binary_search_time(reader, time_lower_bound, lower_bound=True)
        if start_idx is None:
            return 'No data in the ±2 minute range.'  

        for i in range(start_idx, len(reader)):
            row_time = datetime.strptime(reader[i]['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f').replace(second=0, microsecond=0)

            if row_time > time_upper_bound:
                break

            if time_lower_bound <= row_time <= time_upper_bound:
                velocity = float(reader[i]['velocity(m/s)'])
                if max_velocity is None or velocity > max_velocity:
                    max_velocity = velocity

    except FileNotFoundError:
        return 'Data file not found.'
    except Exception as e:
        return f'Error processing data: {e}'

    return max_velocity if max_velocity is not None else 'No data in the ±2 minute range.'
