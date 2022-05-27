% 总产能函数 fun
function res = fun(x)
    % x 为预购量
    
    % 信誉度 c
    load('D:\Base\CodeBase\matlab\data\d3.mat')
    c = da3(:, 7);
    
    % 类别 b
    b = da3(:, 3);
    
    % 不同类别原材料转化为产品的比例 f
    f = [1/0.6 1/0.66 1/0.72];
    
    s =[];
    for i  = 1:size(c,1)
        s = [s,x(i) * c(i) * f(b(i))];
    end
    res = -sum(s);
end