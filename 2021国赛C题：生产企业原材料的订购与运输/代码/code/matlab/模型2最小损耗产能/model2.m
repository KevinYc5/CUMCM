%������
rand('state',sum(clock)); 
p0=0; 
tic     %���浱ǰʱ��
n = 0;
for i=1:10^6 
    x=randi([0,1],19*8,1); % ����1��152�е�����[0,1]�ϵ��������

    [f,g]=mengte(x); 
    if sum(g<=0)==4 %2��3��4��5Լ��������
       if p0<=f     %�ж��Ƿ������Ŀ�꺯��
         x0=x1;     %���ű���
         p0=f;      %����ֵ
      end 
    end 
    if((i-n) >=10^4 )
        n = n + 10^4;
        fprintf('per:  %d     t: %d\n',n/10^4, toc);
    end
end 
x0,p0 
toc    %��¼�������ʱ��
