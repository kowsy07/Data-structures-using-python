class playlist:
    def__init__(self,data):
        self.data=dataself.next=None
class playlist:
    def__init__(self):
        self.head=None
    def append(self,data):
        new_song=song(data)
        if self.head is None:
            self.head=new_song
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_song
        def prepend(self,data):
            new_song=song(data)
            new_song.next=self.head
            self.head=new_song
        def insert(self,position,data):
            new_song=song(data)
            if position<=0:
                print("invalid position")
                return
            if position==1:
                new_song.next=self.head
                self.head=new_song
                return
            current=self.head
            count=1
            while current is not None and count < position -1:
                current=current.next
                count+=1
            if current is None:
                print("invalid position")
                return
            new_song.next=current.next
            current.next=new_song
        def delete(self,data):
            if self.head is None:
                print("playlist is empty.")
                return
            if self.head,data==data
               self.head=self.head.next
                return
            current=self.head
            while current.next:
                if current.next.data=data:
                   current.next=current.next.next
                   return
                current=current.next
            print("song not found.")
        def display(self):
            if self.head is None:
                print("playlist is empty.")
                return
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
            print("None")
        playlist=playlist()
        n=int(input("Enter number of songs:"))
        for i in range(n):
            song=input("Enter a song:")
            playlist.append(song)
        print("\nplaylist:")
        playlist.display()
        choise=input("\ninsert song at beggining or middle(begin/middle):").strip().lower()
        if choice=="begin":
            song=input("Enter a song to insert:")
            playlist.prepend(song)
            print("\nAfter prepend:")
            playlist.display()
        elif choice=="middle":
            position=int(input("Enter position to insert:"))
            song=input("Enter the song to insert:")
            playlist.insert(position,song)
            print("\nAfter insert:") 
            playlist.display()
        else:
            print("invalid choice")
        song=input("\Enter a song to delete:")
        playlist.delete(song)
        print("\nAfter delete:")
        playlist.display()                                   
