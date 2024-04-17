import tkinter
from tkinter import messagebox

class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# GUI Setup
root = tkinter.Tk()
root.title("Counting-out Game")
root.geometry("600x400")

# GUI Variables
eliminationList = []
roundCount = 0

# GUI Functions
def startGame():
    # Reset game if needed
    global eliminationList
    global roundCount
    eliminationList = []
    roundCount = 0

    for i in button:
        i.place_forget()

    # Convert gui entry into integer if possible
    try:
        n = int(n_entry.get())
        k = int(k_entry.get())            
    except:
        messagebox.showinfo(message="Allowed values:\n1<n<12\nk>=1")
    
    # Start game is inputs are valid
    if n > 1 and n < 12 and k >= 1:
        game_info.insert(tkinter.INSERT, f"Game Started. N={n} K={k} \n")

        # Places players buttons in straight line 
        for i in range(n):
            button[i].place(y=25, x=140+(i*40))
        eliminate_button.place(y=80, x=140)

        # Creates circular LinkedList
        head = ListNode(0)
        currentNode = head
        for i in range(1, n):
            currentNode.next = ListNode(i)
            currentNode = currentNode.next
        currentNode.next = head

        # Counting
        lastNode = head
        currentNode = head
        for i in range(n): 
            for i in range(k - 1): 
                lastNode = currentNode
                currentNode = currentNode.next 
            eliminationList.append(currentNode.data) # Adds all players to be removed to elimination list
            lastNode.next = currentNode.next 
            currentNode = lastNode.next
        
    else: 
        messagebox.showinfo(message="Allowed values:\n1<n<12\nk>=1")

def clearGame():
    global eliminationList
    global roundCount
    eliminationList = []
    roundCount = 0
    
    game_info.delete("0.0", tkinter.END) # Clears text widget
    eliminate_button.place_forget()

    for i in button:
        i.place_forget()
    

def removePlayer():
    global roundCount
    roundCount += 1

    if len(eliminationList) > 2:
        game_info.insert(tkinter.INSERT, f"Round {roundCount}: Player {eliminationList[0]} has been eliminated!\n")
        button[eliminationList[0]].place_forget() # Unplaces player widget
        eliminationList.pop(0)
    else: 
        messagebox.showinfo(message=f"Winner: Player {eliminationList[1]}")
        clearGame()

# GUI Widgets
n_label = tkinter.Label(root, text="N")
k_label = tkinter.Label(root, text="K")
n_label.place(x=20, y=20)
k_label.place(x=20, y=50)

n_entry = tkinter.Entry(root, width=5)
k_entry = tkinter.Entry(root, width=5)
n_entry.place(x=40, y=20)
k_entry.place(x=40, y=50)

button = []
for i in range(11):
    button.append(tkinter.Button(root, text=f"{i}", width=4, height=2))

eliminate_button = tkinter.Button(root, text="Eliminate", width=12, height=3, command=removePlayer)

game_info = tkinter.Text(root, height=8)
game_info.pack(fill="x", side=tkinter.BOTTOM)

start_button = tkinter.Button(root, text="Start", width=7, command=startGame)
start_button.place(x=20, y=85)

root.mainloop()