def expression(nums, current_result=0, string=""):
    if not nums:
        print(f"{string}={current_result}")
        return

    expression(nums[1:], current_result+nums[0], f'{string}+{nums[0]}')
    expression(nums[1:], current_result-nums[0], f'{string}-{nums[0]}')



nums = [int(el) for el in input().split(", ")]
expression(nums)