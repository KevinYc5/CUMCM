function [c, ceq] = con1(X)
    load('data/data.mat')
    n_ = 19;
    x = reshape(X, [n_, 24]);
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
    for i = 1:24

        % 进货量 Ei 等于 对企业预购量 * P * f求和
        e = x(:,i);
        su = 0;
        for j = 1:n_
            su = su + e(j) * xy(j) * f(lx(j));
        end
        Ei = su;
        % 库存量 Si 为 Si-1 - 消耗量 + Ei进货量
        if i == 1
            si = 2*cn + Ei - cn;
            s(i) =si;
        else
            si = s(i-1) - cn + Ei;
            s(i) = si;
        end
        
        % 库存量 3 * cost - Si < 0
        c = 3 *cn - s;
        % 
    end

    ceq=[];
end