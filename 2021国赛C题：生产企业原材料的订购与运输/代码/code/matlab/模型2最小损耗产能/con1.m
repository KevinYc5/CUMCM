function [c, ceq] = con1(X)
    load('data/data.mat')
    
    x = reshape(X, [19, 24]);
    % 产能
    cn = 2.82 *10^4;
    % j 的 信誉度
    xy = data(:,6);
    % j 的 材料类型
    lx = data(:,2);
    % 转换率 f
    f = [1/0.6 1/0.66 1/0.72];
    % 一共 24 个约束
    % 库存 si
    s = zeros(1,24);
    c = zeros(1, 24);
    ceq=[];
end