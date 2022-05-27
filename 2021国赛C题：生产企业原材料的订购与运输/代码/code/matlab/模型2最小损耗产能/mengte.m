%函数mengte.m
function [f,g]=mengte(x)
load('data/data.mat')
load('data/sh.mat') % 转运损耗信息
load('D:\Base\CodeBase\matlab\data\e.mat') % 订货数据  e 19 x 24
f=fun(x); 

% 不等式约束
ci = e(:, 1); % 对第一周的转运规划
eq1 = [ci ,zeros(19,7)];
eq = reshape(eq1, 1,8 * 19);
for i = 1:6
    eqi = [zeros(19,i), ci , zeros(19, 7-i)];
    eq = [eq; reshape(eqi, 1,8 * 19)];
end
eq1 = [zeros(19,7),ci ];
eq = [eq; reshape(eq1, 1, 8 * 19)];
A = eq;
b = ones(8, 1) * 6000;

% 等式约束
eq1 = [ones(8,1),zeros(8,18)];
eq = reshape(eq1, 1,8 * 19);
for i = 1:17
    eqi = [zeros(8,i), ones(8,1), zeros(8,18-i)];
    eq = [eq; reshape(eqi, 1,8 * 19)];
end
eq1 = [zeros(8,18),ones(8,1)];
eq = [eq; reshape(eq1, 1, 8 * 19)];

Aeq = eq;
beq = ones(19, 1);

g=[Aeq * x - beq;
    beq - Aeq * x;
    A * x - b]; 

