% �ܳɱ�����
function res = fun(e)
    % ������ e n_ x 24
    n_ = 19;
    reshape(e, n_, 24)
    load('data/data.mat')
    
    % fprintf('X len is %d\n', size(X));
    % ��Ӧ�� j ����Ϣ
    % j �� ������
    xy = data(:,6);
    % j �� ��������
    lx = data(:,2);
    % ���� ��Ӧ�ĵ�λ�ɱ� ------- ��
    %cb = [1.2 1.1 1];
    cb = [4 1.1 1];
    % ����Ӫ�� �����
    tj = sum(e,2);
    % ���� �ܳɱ�
    sum_ = 0;
    for i = 1:n_
        sum_ = sum_ + tj(i) * cb(lx(i)) * xy(i);
    end
    res = sum_;
end