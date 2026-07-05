ticket_number = 0

def get_next_ticket():
    global ticket_number
    ticket_number += 1
    print(f"Клієнт №{ticket_number} запрошується до вікна.")

def reset_queue():
    global ticket_number
    ticket_number = 0
    print("Чергу обнулено!")

get_next_ticket()
get_next_ticket()
get_next_ticket()
reset_queue()
get_next_ticket()