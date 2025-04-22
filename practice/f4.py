def f(name,fav_cri,ipl_team,t=5):
    print(f"{name},your fav team is {ipl_team},and fav cricketer is {fav_cri},has {t} trophies")

f(name='areeb',ipl_team="csk",fav_cri='mahi',t=6)
f(ipl_team='csk',fav_cri='mahi',name='areeb')
f(fav_cri='mahi',name='areeb',ipl_team='csk')