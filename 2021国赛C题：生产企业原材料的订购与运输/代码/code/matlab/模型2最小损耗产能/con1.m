function [c, ceq] = con1(X)
    load('data/data.mat')
    
    x = reshape(X, [19, 24]);
    % ����
    cn = 2.82 *10^4;
    % j �� ������
    xy = data(:,6);
    % j �� ��������
    lx = data(:,2);
    % ת���� f
    f = [1/0.6 1/0.66 1/0.72];
    % һ�� 24 ��Լ��
    % ��� si
    s = zeros(1,24);
    c = zeros(1, 24);
    ceq=[];
end