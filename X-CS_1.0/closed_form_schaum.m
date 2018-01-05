function [ v ] = closed_form_schaum(x,F,E,I)
% ------------------------------------------>8-
% Cf. p. 95/261 Schaum Transformadas de Laplace
% Murray R. SPIEGEL
% 1967
%  x=[0:2000/50:2000];
%  v=closed_form_schaum(x,-10^4,70*10^3,30^4/12);
%  plot(x,v,'b')
%  hold on
%  plot(2000/3,interp1(x,v,2000/3,'linear'),'xr')
%  xlabel('coordinate along x-axis [mm]')
%  ylabel('vertical displacement v [mm]')
% -------------------------------------+------+
%                                      | 2017 |
% -------------------------------------+------+
v=x;
l=x(1,length(x));
c1=+4*F*l/(27*E*I);
c2= -20*F/(27*E*I);
for i = 1:length(x)
    if x(1,i) < x(1,length(x))/3
        v(1,i) = 1/2*c1*(x(1,i))^2+1/6*c2*(x(1,i))^3;
    else
        v(1,i) = 1/2*c1*(x(1,i))^2+1/6*c2*(x(1,i))^3+F/(6*E*I)*(x(1,i)-x(1,length(x))/3)^3;
    end
end