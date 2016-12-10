M = csvread('analysis.csv');

phred = M(1, 1:end);
phred = phred ./ sum(phred);
avgphred = M(2, 1:end);
avgphred = avgphred ./ sum(avgphred);

figure(1)
a = bar(avgphred, 'FaceColor', [0 0.7 0.7]);
hold on;
p = bar(phred);



title('Quality Values of Whole Sample vs Mismatches');
xlabel('Quality Value (Phred - 33)');
ylabel('Relative Frequency of Quality Value');
legend('Average Phred Quality per Base per Read', 'Phred Quality of Mismatched Bases');