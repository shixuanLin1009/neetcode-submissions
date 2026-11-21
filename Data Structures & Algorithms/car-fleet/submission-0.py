class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)  # closest to target first
        fleets = 0
        fleet_time = 0
        for pos, spd in cars:
            t = (target - pos) / spd
            if t > fleet_time:        # can't catch the fleet ahead → new fleet
                fleets += 1
                fleet_time = t
        return fleets
        
# name check:pos_list,min_time

# target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3], expected 3)
# pos_list = [[10,2],[8,4],[5,1],[3,3],[0,1]]
# if not post_list F
# min_time = (target12 - pos_list[0][0]10) /pos_list[0][1]2 = 1
# for pos8,spd4 in pos_list[1:]:
#   time1 = (target12 - pos8)/spd4
#   if time1 > min_time1:F
# for pos5,spd1 in pos_list[1:]:
#   time7 = (target12 - pos5)/spd1
#   if time7 > min_time1:T
#       res += 1,res =2
#       min_time7 = time7
# for pos3,spd3 in pos_list[1:]:
#   time3 = (target12 - pos3)/spd3
#   if time3 > min_time7 F
# for pos0,spd1 in pos_list[1:]:
#   time12 = (target12 - pos0)/spd1
#   if time12 > min_time7 T
#       res += 1, res=3
#       min_time12 = time12
# return res 3