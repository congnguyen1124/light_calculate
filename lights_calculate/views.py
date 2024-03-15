from django.http import JsonResponse
import json

from django.views.decorators.http import require_POST
def find_combinations(nums, target):
    def backtrack(start, path, remain):
        if remain == 0:
            result.append(path)
            return
        if remain < 0:
            return
        for i in range(start, len(nums)):
            backtrack(i, path + [nums[i]], remain - nums[i])

    result = []
    nums.sort()  # Sort the input list to ensure non-decreasing order
    backtrack(0, [], target)
    return result

@require_POST
def calculate_light(request):
     if request.method == 'POST':
        data = json.loads(request.body)
        light_brightness_list = data.get('light_brightness_list', [])
        expected_brightness = data.get('expected_brightness', 0)
        if expected_brightness is not None:
            try:
                expected_brightness = int(expected_brightness)
            except ValueError:
                return JsonResponse({'error': 'Expected brightness must be an integer'}, status=400)
        else:
            return JsonResponse({'error': 'Expected brightness is missing'}, status=400)
        
        setups = find_combinations(light_brightness_list, expected_brightness)
        
        return JsonResponse({'setups': setups}, status=200)
     else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
