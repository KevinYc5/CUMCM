% ��С���ܲ��� ���� fun



% ������ c
load('D:\Base\CodeBase\matlab\data\d3.mat')
c = da3(:, 7);

% ��� b
b = da3(:, 3);

% ��ͬ���ԭ����ת��Ϊ��Ʒ�ı��� f
f_ = [1/0.6 1/0.66 1/0.72];

f =[];
for i  = 1:size(c,1)
    f = [f, - c(i) * f_(b(i))];
end



lb = zeros(1, 384)';
ub = da3(:, 6);

A = c';
b = 8 * 6000;

Aeq = [];
beq = [];

x = linprog(f,A,b,Aeq,beq,lb,ub);

