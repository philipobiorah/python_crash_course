def elevator_floor(enter, exit):
    floor = enter
    elevator_direction = " "

    if enter > exit:
        elevator_direction = "Going down: "

        while floor >= exit:
            elevator_direction += str(floor)

            if(floor > exit):
                elevator_direction += " | "

            floor -= 1


    else:
        elevator_direction = "Going up: "

        while floor <= exit:
            elevator_direction += str(floor)

            if(floor < exit):
                elevator_direction += " | "
            floor += 1    


    return elevator_direction   









# Call the function with 2 integer parameters. 
print(elevator_floor(1,4)) # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6,2)) # Should print Going down: 6 | 5 | 4 | 3 | 2 