clear
clc
load('data/data1.mat')
load('data/sh.mat') % 转运损耗信息
load('D:\Base\CodeBase\matlab\data\e1.mat') % 订货数据  e 348 x 24

nn = 20;

xsum = [];
for i_ = 1: 1


    lb = zeros(nn*8, 1);


    ub = ones(nn*8, 1);
    %ub = [];
    A = [];
    b = [];
    Aeq = [];
    beq = [];

    % 不等式约束
    ci = e1(:, i_); % 对第一周的转运规划
    eq1 = [ci' ;zeros(7,nn)];
    eq = reshape(eq1, 1,8 * nn);
    for i = 1:6
        eqi = [zeros(i,nn); ci' ; zeros(7-i, nn)];
        eq = [eq; reshape(eqi, 1,8 * nn)];
    end
    
    eq1 = [zeros(7,nn);ci' ];
    eq = [eq; reshape(eq1, 1, 8 * nn)];
    A = eq;
    b = ones(8, 1) * 6000;

    % 等式约束
    eq1 = [ones(8,1),zeros(8,nn-1)];
    eq = reshape(eq1, 1,8 * nn);
    for i = 1:nn-2
        eqi = [zeros(8,i), ones(8,1), zeros(8,nn-1-i)];
        eq = [eq; reshape(eqi, 1,8 * nn)];
    end
    
    eq1 = [zeros(8,nn-1),ones(8,1)];
    eq = [eq; reshape(eq1, 1, 8 * nn)];

    Aeq = eq;
    beq = ones(nn, 1);

    options = optimoptions('fmincon','Display','iter','Algorithm','sqp');

    % 计算 线性规划的系数
    w = sh;                     % 转运损耗向量 W 
    ci = e1(:, 1);               % 对第一周的转运规划
    xy = data1(:,6);         % j 的 信誉度
    lx = data1(:,2);         % j 的 材料类型
    % 材料 对应的单位成本
    cb = [1.2 1.2 1];
    % 转换率 f
    f = [1/0.6 1/0.66 1/0.72];
    % 成本  = wT* Q * c .* xy.*f 
    temp = ci .* xy .* f(lx)';

    f1= [];
    for i = 1:nn
        for j = 1:8
            f1 = [f1, temp(i) * w(j)];
        end
    end

    intcon= [1:nn*8];
    x = intlinprog(f1,intcon,A,b,Aeq,beq,lb,ub);
    

    xsum = [xsum, x];
end

