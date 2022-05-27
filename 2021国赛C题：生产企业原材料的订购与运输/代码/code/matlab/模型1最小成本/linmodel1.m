load('data/data.mat')

% fprintf('X len is %d\n', size(X));
% ��Ӧ�� j ����Ϣ
% j �� ������
xy = data(:,6);
% j �� ��������
lx = data(:,2);
% ���� ��Ӧ�ĵ�λ�ɱ� ------- ��
%cb = [1.2 1.1 1];
cb = [0.1 1.1 1];
% ������ e n_ x 24
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


