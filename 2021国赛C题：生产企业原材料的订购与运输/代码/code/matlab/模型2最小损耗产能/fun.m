% ���� �����������
function res = fun(q)
    load('data/data.mat')
    load('data/sh.mat') % ת�������Ϣ
    load('D:\Base\CodeBase\matlab\data\e.mat') % ��������  e 19 x 24
    w = sh; % ת��������� W
    
    ci = e(:, 1); % �Ե�һ�ܵ�ת�˹滮
    
    % ��Ӧ�� j ����Ϣ
    % j �� ������
    xy = data(:,6);
    
    % j �� ��������
    lx = data(:,2);
    % ���� ��Ӧ�ĵ�λ�ɱ�
    cb = [1.2 1.2 1];
    % ת���� f
    f = [1/0.6 1/0.66 1/0.72];
        
    % 01���߾��� Q 8 * 19
    q =  reshape(q, 8, 19);
    
    % �ɱ�  = wT* Q * c .* xy.*f 
    temp = ci .* xy .* f(lx)';
    res = w' * q * temp;

end