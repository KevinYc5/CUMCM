% �ܲ��ܺ��� fun
function res = fun(x)
    % x ΪԤ����
    
    % ������ c
    load('D:\Base\CodeBase\matlab\data\d3.mat')
    c = da3(:, 7);
    
    % ��� b
    b = da3(:, 3);
    
    % ��ͬ���ԭ����ת��Ϊ��Ʒ�ı��� f
    f = [1/0.6 1/0.66 1/0.72];
    
    s =[];
    for i  = 1:size(c,1)
        s = [s,x(i) * c(i) * f(b(i))];
    end
    res = -sum(s);
end