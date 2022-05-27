
clear
clc
load('data/data.mat')

n_ = 19;

x0 = data(:,5)*0.5;
x0 = repmat(x0,1, 24);
% rng(1);
x0 = reshape(x0, n_*24,1) + rand(n_*24,1) * 100;

nonlcon = @con1;
lb = zeros(n_, 24);
lb = reshape(lb, n_*24,1);

% 供应能力
a = 3;
nl = data(:,5) * a;
ub = repmat(nl,1, 24);
ub = reshape(ub, n_*24,1);
%ub = [];
A = [];
b = [];
Aeq = [];
beq = [];


options = optimoptions('fmincon','Display','iter','Algorithm','active-set');
x = fmincon(@fun,x0,A,b,Aeq,beq,lb,ub,nonlcon,options);

x = reshape(x, n_,24);
