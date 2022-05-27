%主函数
rand('state',sum(clock)); 
p0=0; 
tic     %保存当前时间
n = 0;
for i=1:10^6 
    x=randi([0,1],19*8,1); % 产生1行152列的区间[0,1]上的随机整数

    [f,g]=mengte(x); 
    if sum(g<=0)==4 %2，3，4，5约束都满足
       if p0<=f     %判断是否最大了目标函数
         x0=x1;     %最优变量
         p0=f;      %最优值
      end 
    end 
    if((i-n) >=10^4 )
        n = n + 10^4;
        fprintf('per:  %d     t: %d\n',n/10^4, toc);
    end
end 
x0,p0 
toc    %记录程序完成时间
