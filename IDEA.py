import io
import sys

idea_list=[]
i=1

def add_ideas(i=i):
    while True:
        a=input("What is your new idea?")
        if a=="--list":
            print("Twoje aktualne pomysły:", idea_list)
        elif a[0:8]=="--delete":
            if len(a)<9:
                print("Specify a number after --delete.")
            else:
                b=int(a[-1])
                if b>=i:
                    print(f'The list contains only {i-1} ideas, but youre attempting to delete an idea number {b}.')
                else:
                    idea_list.pop(b-1)
        else:
            a=(str(i)+". "+a)
            idea_list.append(a)
            with open('ideas.txt','a+',encoding='utf-8') as f:
                f.write(a)
                f.write('\n')
                f.close()
            i+=1
            print("Twoje aktualne pomysły:", idea_list)

add_ideas()