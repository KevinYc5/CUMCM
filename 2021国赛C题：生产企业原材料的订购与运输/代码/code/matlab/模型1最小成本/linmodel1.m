load('data/data.mat')

% fprintf('X len is %d\n', size(X));
% 供应商 j 的信息
% j 的 信誉度
xy = data(:,6);
% j 的 材料类型
lx = data(:,2);
% 材料 对应的单位成本 ------- 改
%cb = [1.2 1.1 1];
cb = [0.1 1.1 1];
% 订购量 e n_ x 24
n_ = 19;

x0 = ones(19*24,1);

f = zeros(19*24,1);
for i = 1:19*24
    f(i) = cb(lx(mod(i-1,n_)+1)) * xy(mod(i-1,19)+1);
end

nonlcon = @con1;
lb = zeros(n_, 24);
lb = reshape(lb, n_*24,1);

a = 2;
nl = data(:,5) * a;
ub = repmat(nl,1, 24);
ub = reshape(ub, n_*24,1);

A = [];
b = [];
Aeq = [];
beq = [];

options = optimoptions('linprog','Display','iter');
x = linprog(f,x0,A,b,Aeq,beq,lb,ub,[],options);


