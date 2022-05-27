function [c, ceq] = con1(X)
    load('data/data.mat')
    n_ = 19;
    x = reshape(X, [n_, 24]);
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
    for i = 1:24

        % ������ Ei ���� ����ҵԤ���� * P * f���
        e = x(:,i);
        su = 0;
        for j = 1:n_
            su = su + e(j) * xy(j) * f(lx(j));
        end
        Ei = su;
        % ����� Si Ϊ Si-1 - ������ + Ei������
        if i == 1
            si = 2*cn + Ei - cn;
            s(i) =si;
        else
            si = s(i-1) - cn + Ei;
            s(i) = si;
        end
        
        % ����� 3 * cost - Si < 0
        c = 3 *cn - s;
        % 
    end

    ceq=[];
end