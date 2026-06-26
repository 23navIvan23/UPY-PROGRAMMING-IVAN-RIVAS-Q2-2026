# Full School Management System
# Compatible with Thonny

users = {
    "lescalante":{"password":"1234","role":"student","name":"Luis Escalante"},
    "afigueroa":{"password":"1234","role":"student","name":"Alejandro Figueroa"},
    "adardon":{"password":"1234","role":"student","name":"Arcadio Dardón"},
    "irivas":{"password":"1234","role":"student","name":"Iván Rivas"},
    "kpool":{"password":"1234","role":"student","name":"Keyra Pool"},
    "ccab":{"password":"1234","role":"student","name":"Cristian Cab"},
    "jpedrozo":{"password":"1234","role":"teacher","name":"Jorge Pedrozo Romero"},
    "rgarcia":{"password":"1234","role":"coordinator","name":"Rosa García"}
}

subjects=(
"Programming",
"Social Emotional Skills and Conflict Management",
"Probability and Statistics",
"Computer and Server Architecture",
"Tutoring",
"Differential Calculus",
"Discrete Math",
"English II"
)

grades={
"lescalante":{"Programming":9.4,"Social Emotional Skills and Conflict Management":8.6,"Probability and Statistics":7.2,"Computer and Server Architecture":9.1,"Tutoring":10.0,"Differential Calculus":6.8,"Discrete Math":8.9,"English II":9.3},
"afigueroa":{"Programming":5.6,"Social Emotional Skills and Conflict Management":7.0,"Probability and Statistics":6.2,"Computer and Server Architecture":8.7,"Tutoring":10.0,"Differential Calculus":4.8,"Discrete Math":7.1,"English II":8.8},
"adardon":{"Programming":8.3,"Social Emotional Skills and Conflict Management":9.5,"Probability and Statistics":8.9,"Computer and Server Architecture":6.4,"Tutoring":10.0,"Differential Calculus":8.1,"Discrete Math":5.9,"English II":7.5},
"irivas":{"Programming":10.0,"Social Emotional Skills and Conflict Management":9.8,"Probability and Statistics":9.6,"Computer and Server Architecture":9.7,"Tutoring":10.0,"Differential Calculus":9.4,"Discrete Math":9.8,"English II":10.0},
"kpool":{"Programming":7.0,"Social Emotional Skills and Conflict Management":8.4,"Probability and Statistics":5.7,"Computer and Server Architecture":7.8,"Tutoring":10.0,"Differential Calculus":8.3,"Discrete Math":6.6,"English II":8.6},
"ccab":{"Programming":9.7,"Social Emotional Skills and Conflict Management":9.2,"Probability and Statistics":8.8,"Computer and Server Architecture":9.0,"Tutoring":10.0,"Differential Calculus":7.0,"Discrete Math":6.9,"English II":9.8}
}

logged=False
while not logged:
    u=input("Username: ")
    p=input("Password: ")
    if u in users and p==users[u]["password"]:
        logged=True
        role=users[u]["role"]
        name=users[u]["name"]
        if role=="teacher":
            print("\nWelcome Professor",name)
        else:
            print("\nWelcome",name)
    else:
        print("Invalid credentials\n")

if role=="student":
    approved=set()
    print("\nREPORT CARD")
    for s in subjects:
        g=grades[u][s]
        print(f"{s}: {g}")
        if g>=7:
            approved.add(s)
    pending=set(subjects)-approved
    print("\nApproved:",approved)
    print("Pending:",pending)

elif role=="teacher":
    teacher=True
    while teacher:
        print("\nSTUDENTS")
        for k,v in users.items():
            if v["role"]=="student":
                print(k,"-",v["name"])
        student=input('\nStudent username\nDo you want to close your session? (Type "Exit")\n> ')
        if student.lower()=="exit":
            break
        if student not in grades:
            print("Student not found.")
            continue
        while True:
            print("\nSUBJECTS")
            for s in subjects:
                print("-",s)
            subject=input('\nSubject\nType "Back" to choose another student.\nDo you want to close your session? (Type "Exit")\n> ')
            if subject.lower()=="exit":
                teacher=False
                break
            if subject.lower()=="back":
                break
            if subject not in subjects:
                print("Invalid subject.")
                continue
            while True:
                try:
                    new=float(input("New grade: "))
                except:
                    print("Invalid grade.")
                    continue
                print("\nCurrent:",grades[student][subject])
                print("New:",new)
                op=input('yes/no/back/exit: ').lower()
                if op=="yes":
                    grades[student][subject]=new
                    print("Grade updated!")
                    break
                elif op=="no":
                    continue
                elif op=="back":
                    break
                elif op=="exit":
                    teacher=False
                    break
            if not teacher or op=="back" or op=="yes":
                break
    print("Closing session...")

elif role=="coordinator":
    print("\nTEACHERS")
    for k,v in users.items():
        if v["role"]=="teacher":
            print("-",v["name"])
    print("\nGRADE REPORT")
    print("="*135)
    print(f'{"Student":25}{"Prog":>8}{"SESCM":>8}{"Prob":>8}{"Arch":>8}{"Tutor":>8}{"Calc":>8}{"Disc":>8}{"EngII":>8}')
    print("="*135)
    for st in grades:
        row=f'{users[st]["name"]:25}'
        fails=0
        for s in subjects:
            val=grades[st][s]
            txt=f"{val:.1f}"
            if val<7:
                txt+="*"
                fails+=1
            row+=f"{txt:>8}"
        row+=f"   Failed:{fails}"
        print(row)
    print("="*135)
    print("* Grade below 7.0 = Failed")

print("\nProgram finished.")
