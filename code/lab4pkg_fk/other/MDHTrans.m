%modified DH Transform
function T = MDHTrans(alpha, a, d, theta)
if alpha == pi/2 || alpha == -pi/2
    T=[cos(theta),-sin(theta),0,a;
       sin(theta)*0,cos(theta)*0,-sin(alpha),-sin(alpha)*d;
       sin(theta)*sin(alpha),cos(theta)*sin(alpha),0,0*d;
       0,0,0,1];
else
    T=[cos(theta),-sin(theta),0,a;
       sin(theta)*cos(alpha),cos(theta)*cos(alpha),-sin(alpha),-sin(alpha)*d;
       sin(theta)*sin(alpha),cos(theta)*sin(alpha),cos(alpha),cos(alpha)*d;
       0,0,0,1];
end
end