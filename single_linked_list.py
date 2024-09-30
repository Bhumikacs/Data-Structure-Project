from tkinter import *
from tkinter import messagebox

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Single Linked List class
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.max_size = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        if self.max_size is not None and self.size >= self.max_size:
            messagebox.showerror("Error", "Linked list has reached its maximum size")
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        if self.max_size is not None and self.size >= self.max_size:
            messagebox.showerror("Error", "Linked list has reached its maximum size")
            return
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        self.head = self.head.next
        self.size -= 1
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            self.size -= 1
            return deleted_node.data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        self.size -= 1
        return deleted_node.data

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# GUI application class
class LinkedListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Data Structure")
        self.root.state("zoomed")
        self.root['bg'] = 'light blue'

        self.linked_list = SingleLinkedList()

        # Configuring grid layout
        self.root.columnconfigure((0, 1, 2, 3, 4, 5), weight=10)
        self.root.rowconfigure((0, 1, 2, 3, 4, 5), weight=10)

        # Initialize UI components
        Label(root, text="Enter the number:").grid(row=0, column=0, padx=10, pady=10, sticky=E)
        self.input_entry = Entry(root)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        Label(root, text="Set Linked List size:").grid(row=0, column=2, padx=10, pady=10, sticky=E)
        self.size_entry = Entry(root)
        self.size_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        Button(root, text="Set Size", command=self.set_linked_list_size).grid(row=0, column=4, padx=10, pady=10, sticky=W)
        Button(root, text="Insert at Beginning", command=self.insert_at_beginning).grid(row=1, column=0, padx=10, pady=10)
        Button(root, text="Insert at End", command=self.insert_at_end).grid(row=1, column=1, padx=10, pady=10)
        Button(root, text="Delete at Beginning", command=self.delete_at_beginning).grid(row=1, column=2, padx=10, pady=10)
        Button(root, text="Delete at End", command=self.delete_at_end).grid(row=1, column=3, padx=10, pady=10)
        Button(root, text="Is Empty", command=self.is_empty).grid(row=1, column=4, padx=10, pady=10)

        # Canvas for visualization
        self.canvas = Canvas(root, width=800, height=500, bg='white')
        self.canvas.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

    # Set the maximum size of the linked list
    def set_linked_list_size(self):
        try:
            size = int(self.size_entry.get())
            if size <= 0:
                raise ValueError
            self.linked_list.max_size = size
            messagebox.showinfo("Success", f"Linked list size set to {size}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for linked list size")

    # Insert at the beginning
    def insert_at_beginning(self):
        data = self.input_entry.get()
        if data:
            self.linked_list.insert_at_beginning(data)
            self.update_visualization()

    # Insert at the end
    def insert_at_end(self):
        data = self.input_entry.get()
        if data:
            self.linked_list.insert_at_end(data)
            self.update_visualization()

    # Delete from the beginning
    def delete_at_beginning(self):
        deleted_data = self.linked_list.delete_at_beginning()
        if deleted_data is not None:
            messagebox.showinfo("Deleted", f"{deleted_data} deleted from the beginning")
            self.update_visualization()

    # Delete from the end
    def delete_at_end(self):
        deleted_data = self.linked_list.delete_at_end()
        if deleted_data is not None:
            messagebox.showinfo("Deleted", f"{deleted_data} deleted from the end")
            self.update_visualization()

    # Check if the list is empty
    def is_empty(self):
        if self.linked_list.is_empty():
            messagebox.showinfo("Empty", "Linked list is empty")
        else:
            messagebox.showinfo("Not Empty", "Linked list is not empty")

    # Update the canvas visualization
    def update_visualization(self):
        self.canvas.delete("all")
        node = self.linked_list.head
        y = 50
        while node:
            self.canvas.create_rectangle(100, y, 300, y + 30, fill="lightblue")
            self.canvas.create_text(200, y + 15, text=str(node.data), font=("Helvetica", 12))
            y += 40
            node = node.next

    def run(self):
        self.root.mainloop()
    def create_new_window(self):
        self.destroy_window()  # Close the current window
        new_root = Tk()
        new_app = LinkedListApp(new_root)  # Create a new instance of the app
        new_root.attributes('-topmost', True)  # Bring new window to the front
        new_root.mainloop()

    def destroy_window(self):
        self.root.destroy()  # Close the current window
# Running the application
if __name__ == "__main__":
    root = Tk()
    app = LinkedListApp(root)
    app.run()
