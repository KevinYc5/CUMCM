t = zeros(1, 25);
tt = sortrows(e3,1);
sum1 = [];
for i = 0 : 401
    a = 0;
    for j = 1:348
        if i == tt(j,1)
            sum1 = [sum1;tt(j,:)];
            a = 1;
            break;
        end
    end
    if a == 0
        sum1 = [sum1;t];
    end
end