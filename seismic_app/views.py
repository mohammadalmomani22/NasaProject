import json  # Import the json module
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import csv
import os
from datetime import datetime, timedelta
from django.conf import settings

@csrf_exempt  # Disable CSRF protection for this view
def seismic_data_view(request):
    if request.method == 'POST':
        results = []

        try:
            # Parse the JSON request body
            data = json.loads(request.body)
            from_date_str = data['from_date']
            to_date_str = data['to_date']

            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')

            if from_date > to_date:
                return JsonResponse({'error': 'From date must be earlier than To date.'}, status=400)

            csv_file_path = os.path.join(settings.BASE_DIR, 'space_apps_2024_seismic_detection', 'data', 'lunar', 'training', 'catalogs', 'apollo12_catalog_GradeA_final.csv')
            with open(csv_file_path, 'r') as csvfile:
                reader = list(csv.DictReader(csvfile))

            for row in reader:
                event_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f')
                if from_date <= event_time <= to_date:
                    # Check if max_velocity is already filled
                    max_velocity = row.get('max_velocity', None)
                    if max_velocity:
                        results.append({
                            'filename': row['filename'],
                            'event_time': event_time,
                            'max_velocity': max_velocity,
                            'mq_type': row['mq_type'],
                        })
                    else:
                        # Calculate max_velocity if it was not filled
                        max_velocity = get_max_velocity(row['filename'], event_time)
                        results.append({
                            'filename': row['filename'],
                            'event_time': event_time,
                            'max_velocity': max_velocity,
                            'mq_type': row['mq_type'],
                        })

            return JsonResponse({'results': results}, status=200)

        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

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
                try:
                    # Check for valid velocity
                    velocity = float(reader[i]['velocity(m/s)'])  # Ensure this matches your CSV column name
                    if velocity is not None and (max_velocity is None or velocity > max_velocity):
                        max_velocity = velocity
                except (ValueError, TypeError):
                    # Skip this entry if the velocity is invalid
                    continue

    except FileNotFoundError:
        return 'Data file not found.'
    except Exception as e:
        return f'Error processing data: {e}'

    return max_velocity if max_velocity is not None else 'No valid data in the ±2 minute range.'

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
