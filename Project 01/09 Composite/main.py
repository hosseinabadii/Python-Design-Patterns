from composite import Composite, Child

#--------------------------------
sub1 = Composite('menu1')

sub1_1 = Child('sub_menu1_1')
sub1_2 = Child('sub_menu1_2')
sub1_3 = Child('sub_menu1_3')

sub1.append_child(sub1_1)
sub1.append_child(sub1_2)
sub1.append_child(sub1_3)

#--------------------------------
sub2 = Composite('menu2')

sub2_1 = Child('sub_menu2_1')
sub2_2 = Child('sub_menu2_2')
sub2_3 = Child('sub_menu2_3')

sub2.append_child(sub2_1)
sub2.append_child(sub2_2)
sub2.append_child(sub2_3)

#---------------------------
top = Composite('top menu')
top.append_child(sub1)
top.append_child(sub2)
top.component_function()
