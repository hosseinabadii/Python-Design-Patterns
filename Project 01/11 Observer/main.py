from observer import Core, TempObserver

main_core = Core('Main Core')

o1 = TempObserver('Observer 1', access=True)
o2 = TempObserver('Observer 2')
o3 = TempObserver('Observer 3')

main_core.attach(o1)
main_core.attach(o2)
main_core.attach(o3)

main_core.change_temp(o3, 100)
main_core.change_temp(o1, 100)

main_core.detach(o3)
main_core.change_temp(o3, 300)

main_core.change_temp(o1, 500)
