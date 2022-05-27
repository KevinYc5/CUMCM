% 总成本函数
function res = fun(e)
    % 订购量 e n_ x 24
    n_ = 19;
    reshape(e, n_, 24)
    load('data/data.mat')
    
    % fprintf('X len is %d\n', size(X));
    % 供应商 j 的信息
    % j 的 信誉度
    xy = data(:,6);
    % j 的 材料类型
    lx = data(:,2);
    % 材料 对应的单位成本 ------- 改
    %cb = [1.2 1.1 1];
    cb = [4 1.1 1];
    % 各运营商 总体积
    tj = sum(e,2);
    % 计算 总成本
    sum_ = 0;
    for i = 1:n_
        sum_ = sum_ + tj(i) * cb(lx(i)) * xy(i);
    end
    res = sum_;
end