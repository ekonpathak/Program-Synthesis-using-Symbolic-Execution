    print ("*************")
    print(ir)
    print(args.progfl)
    print ("*************")
     # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,y>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print ("*************")
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    s.addAssignment('x','70')
    s.addAssignment('y','90')

    # To get any variable assigned
    
    print(s.s.check())
    print(s.s.solver.value)
    print ("*************")
    print("variable assignment of z =",s.getVar('z'))
    print("variable assignment of x =",s.getVar('x'))
    print("variable assignment of y =",s.getVar('y'))
    x = Int('x')
    y = Int('y')
    print( simplify (x + y + 2*x + 3))

    
    c1 = Real('c1')
    c2 = Real('c2')

    
    eq1 =  simplify ( Implies ( x<=42 , y == x  + c1  )  )
    eq2 =  simplify ( Implies ( x<=42 , y == x  + 22  )  )
    eq11 = simplify ( Implies ( x>42  , y == x  + c2  )  )
    eq22 = simplify ( Implies ( x>42  , y == x  + 40  )  ) 
    print(eq1)
    print(eq2)
    solve (  eq1 ,eq2 )
    solve ( eq11 , eq22 )
    
    
    solve(x**2 + y**2 > 3, x**3 + y < 5)   
    x = Real('x')
    solve ( x > 4 , x < 0 ) 
    p = Bool('p')
    q = Bool('q')
    print (And(p, q, True))
    print (simplify(And(p, q, False)))
    print (simplify(And(p, False)))
    