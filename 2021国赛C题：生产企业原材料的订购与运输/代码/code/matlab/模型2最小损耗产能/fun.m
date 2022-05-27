% 返回 总损耗量函数
function res = fun(q)
    load('data/data.mat')
    load('data/sh.mat') % 转运损耗信息
    load('D:\Base\CodeBase\matlab\data\e.mat') % 订货数据  e 19 x 24
    w = sh; % 转运损耗向量 W
    
    ci = e(:, 1); % 对第一周的转运规划
    
    % 供应商 j 的信息
    % j 的 信誉度
    xy = data(:,6);
    
    % j 的 材料类型
    lx = data(:,2);
    % 材料 对应的单位成本
    cb = [1.2 1.2 1];
    % 转换率 f
    f = [1/0.6 1/0.66 1/0.72];
        
    % 01决策矩阵 Q 8 * 19
    q =  reshape(q, 8, 19);
    
    % 成本  = wT* Q * c .* xy.*f 
    temp = ci .* xy .* f(lx)';
    res = w' * q * temp;

end