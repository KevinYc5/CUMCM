su = zeros(19,1);
for j = 1:19
    tmp = sum(x(j,:));
    su(j) = tmp;
end
su = su/ 24;

% 排序
id_su = [data(:,1:2),su];
id_su = sortrows(id_su,2);

% 分组求和
sum1 = zeros(1,3);
for j = 1:19
    if id_su(j,2) == 1
        sum1(1) = sum1(1) + id_su(j,3);
    elseif id_su(j,2) == 2
        sum1(2) = sum1(2) + id_su(j,3);
    else
        sum1(3) = sum1(3) + id_su(j,3);
    end
end

ab = sum1(1)/sum1(3);


% --------供应能力 = 3 * data(:,5)-------------
% a = 0.5
%[1.25053859444714]

% a = 1
%[1.24025882266888]

% a = 1.5
% [1.10447226722918]

% a = 2
% [1.10674567848540]
% 

% a = 3 
% [1.07289835921341]

% a = 4
% [1.09904625188386]
