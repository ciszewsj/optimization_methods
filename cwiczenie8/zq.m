clear all
close all
clc
load('LM01Data.mat')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


k_max = 35;
h = @(x,t) x(1)*sin(x(2)*t+x(3));
f = @(x) x(1)*sin(x(2)*t+x(3))-y;
x0 = [1.0, 100*pi, 0.0]'; % initial values of model parameters
n = length(x0);
figure
plot01 = plot(t,y,"s","MarkerEdgeColor","r","MarkerFaceColor","r");
hold on
tPlot = linspace(t(1),t(end),1e+3)';
plot02 = plot(tPlot,h(x0,tPlot),"b","LineWidth",2);
grid on
J = @(x) [sin(x(2)*t+x(3)) x(1)*t.*cos(x(2)*t+x(3)) x(1)*cos(x(2)*t+x(3))];
X = zeros(n,k_max+1);
X(:,1) = x0;

L = 1.0;
L_history = zeros(k_max+1);
obj_f_history = zeros(k_max+1);
L_history(1) = L;
obj_f_history(1) = sum(f(X(:,1)).^2);
for k = 1:k_max
    x = X(:,k);
    xNew = x - ((J(x)'*J(x)) + L*eye(n))\J(x)'*f(x);
    if ( norm(f(xNew)) < norm(f(x0)) )
        X(:,k+1) = xNew;
        L = 0.8*L;
    else
        X(:,k+1) = x;
        L = 2*L;
    end
    L_history(k+1) = L;
    obj_f_history(k+1) = sum(f(X(:,k+1))).^2;
end

xOptimal = X(:,end);

nfontslatex = 16;

plot03 = plot(tPlot,h(xOptimal,tPlot),"k","LineWidth",2);
legend([plot01,plot02,plot03],"measurement", "first guess", "final fit")
%set(gca,"FontSize",nfonts);
ylabel("$y = A\sin(\omega t + \phi)$ [a.u.]","Interpreter","Latex","FontSize",nfontslatex)
xlabel("$t$ [s]","Interpreter","Latex","FontSize",nfontslatex)
figure
%set(gca,"FontSize",nfonts);
subplot(3,1,1)
plot((0:k_max),X(1,:),"k","LineWidth",2)
ylabel("$A$ [a.u.]","Interpreter","Latex","FontSize",nfontslatex)
subplot(3,1,2)
plot((0:k_max),X(2,:),"k","LineWidth",2)
ylabel("$\omega$ [rad/s]","Interpreter","Latex","FontSize",nfontslatex)
subplot(3,1,3)
plot((0:k_max),X(3,:),"k","LineWidth",2)
ylabel("$\varphi$ [rad]","Interpreter","Latex","FontSize",nfontslatex)
xlabel("iteration number","Interpreter","Latex","FontSize",nfontslatex)


figure
plot04 = plot(0:k_max,L_history,'s');
grid on
ylabel("λ^k")
xlabel("k")



figure

plot05 = plot(0:k_max,obj_f_history,'s');
grid on
ylabel("||f(x)||^2")
xlabel("k")


