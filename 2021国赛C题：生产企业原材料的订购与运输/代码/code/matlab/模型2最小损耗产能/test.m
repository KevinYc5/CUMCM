ci = e(:, 1); % 对第一周的转运规划
eq1 = [ci ,zeros(19,7)];
eq = reshape(eq1, 1,8 * 19);
for i = 1:6
    eqi = [zeros(19,i), ci , zeros(19, 7-i)];
    eq = [eq; reshape(eqi, 1,8 * 19)];
end
eq1 = [zeros(19,7),ci ];
eq = [eq; reshape(eq1, 1, 8 * 19)];