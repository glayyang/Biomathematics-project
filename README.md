# Biomathematics-project
This was a final project with the prompt to create a mathematical model with biological implications. The full report will be linked:
[Biol301_finalproject_glay.pdf](https://github.com/glayyang/Biomathematics-project/files/10550858/Biol301_finalproject_glay.pdf)

Maxima was the software used to code the math and plot phase planes. As GitHub doesn't support Maxima files the code will be entered below:

Basic math done to solve for equilibria (ahat and phat) of the equations developed in the report:

 -->	solve(A=(1+r2)*A-ρ2*P*A, A);

 -->	phat: solve(A=(1+r2)*A-ρ2*P*A, P);

 -->	solve(P=(1+r1)*P-ρ1*P*A+m, P);

 -->	solve(P=(1+r1)*P-ρ1*P*A+m, A);

 -->	ahat: solve(P=(1+r1)*P-ρ1*P*A + m, A), P:r2/ρ2;

 -->	solve(P=(1+r1)*P-ρ1*P*A + m, P), A:0;

Partial derivatives:
	
 -->	aeq:(1+r2)*A-ρ2*P*A;
 
peq:(1+r1)*P-ρ1*P*A + m;


 -->	dAA: diff(aeq,A);
 

 -->	dAP: diff(aeq,P);


 -->	dPA: diff(peq,A);


 -->	dPP: diff(peq,P);


Jacobian matrix:
	
 -->	J: matrix([dPP, dPA], [dAP, dAA]);

 -->	J1e: matrix([ratsimp(subst(A=(m*ρ2+r1*r2)/(r2*ρ1),dPP)), subst(P=r2/ρ2,dPA)], [(subst(A=(m*ρ2+r1*r2)/(r2*ρ1),dAP)), ratsimp(subst(P=r2/ρ2,dAA))]);

 -->	eigenvalues(J1e);

 -->	[eigenvalue1, eigenvalue2]: eigenvalues(J1e)[1];

 -->	subst([m=10, r1=0.1, r2=0.9, ρ2=0.1], eigenvalue1);

 -->	subst([m=10, r1=0.1, r2=0.9, ρ2=0.1], eigenvalue2);


Determinant & characteristic polynomial analysis:
	
 -->	Jlam: matrix([ratsimp(subst(A=(m*ρ2+r1*r2)/(r2*ρ1),dPP))-lam, subst(P=r2/ρ2,dPA)], [(subst(A=(m*ρ2+r1*r2)/(r2*ρ1),dAP)), ratsimp(subst(P=r2/ρ2,dAA))-lam]);

 -->	determinant(Jlam);

 -->	factor(ratsimp(solve(determinant(Jlam)=0, lam)));


Model, i.e. equations to plot:
	
	Pythons: P[t+1] = (1 + r1)P[t] - ϱ1P[t]A[t] + m
	
	Alligators: A[t+1] = (1 + r2)A[t] - ϱ2P[t]A[t]
	
  
  Here is the rough work done to code the plots. The parameters are free to play around with and will net very different plots depending on the values. I've addressed some of the issues with this in the report. Note that Maxima is fairly buggy and under certain conditions will not plot graphs even if they are coded correctly.
  
  -->	(2*r1+m*p2+2*r2)^2;

 -->	popP[pars, t] :=  block([r1:pars[1], r2:pars[2], ϱ1:pars[3], ϱ2:pars[4], P0:pars[5], A0:pars[6], m:pars[7]], 
	    if t=0 then P0 else if (tempP:(1+r1)*popP[pars, t-1] - ϱ1*popP[pars, t-1]*popA[pars, t-1]+m)>0 then tempP else 0);
	popA[pars, t] :=  block([r1:pars[1], r2:pars[2], ϱ1:pars[3], ϱ2:pars[4], P0:pars[5], A0:pars[6], m:pars[7]], 
	    if t=0 then A0 else if (tempA:(1+r2)*popA[pars, t-1] - ϱ2*popP[pars, t-1]*popA[pars, t-1])>0 then tempA else 0);
	;

 -->	popA[[r1:0.1, r2:0.1, ϱ1:0.0005, ϱ2:0.0005, P0:100, A0:100, m:10], 2];
(popA[[r1)	109.4625

 -->	list: makelist([popP[[r1:0.1, r2:0.1, ϱ1:0.0005, ϱ2:0.0005, P0:100, A0:100, m:10], t],popA[[r1:0.1, r2:0.1, ϱ1:0.0005, ϱ2:0.0005, P0:100, A0:100, m:10], t]], t, 0, 50)$
	wxplot2d([discrete, list], [t, 0, 50], [xlabel, "Pythons"], [ylabel, "Alligator"]);

 -->	list_p: makelist(list[i][1],i,1,50)$
	wxplot2d([discrete,list_p], [xlabel, "Time"], [ylabel, "Number of Pythons"]);

 -->	list_p: makelist(list[i][2],i,1,50)$
	wxplot2d([discrete,list_p], [xlabel, "Time"], [ylabel, "Number of Alligators"]);
