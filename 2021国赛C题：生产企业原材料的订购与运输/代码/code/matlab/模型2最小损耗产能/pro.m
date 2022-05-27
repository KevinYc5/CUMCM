load('D:\Base\CodeBase\matlab\data\data.mat')
load('D:\Base\CodeBase\matlab\data\e.mat') % ¶©»õÊý¾Ý  e 
% load('D:\Base\CodeBase\matlab\data\xsum.mat')
res_ = [];
nn = 19;

temp = zeros(nn, 8);

for i = 1 : 24
    ei = e(:,i);
    q = reshape(xsum(:,i), 8, nn);
    res = [];
    for j = 1 : nn
        resj =q(:,j)' * ei(j);
        res = [res;resj];
    end
    res_ = [res_,res];
    temp = temp + res;
end

temp = temp /24;
temp = [data(:,2), temp];
temp = sortrows(temp, 1);
temp = temp(:, 2:9);
aa = temp(1:6,:);
bb = temp(7:13,:);
cc = temp(14:19,:);
as = sum(aa);
bs = sum(bb);
cs = sum(cc);
da = [as;bs;cs]';

%re = sum(temp);




