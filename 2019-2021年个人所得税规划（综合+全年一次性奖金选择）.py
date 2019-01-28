#!/usr/bin/env python
# coding: utf-8


# 导入必要的包
import time

# 设置系统参数
start_time = time.clock()  # 适用于统计cpu运行时间
# 导入数据方式一：直接初始化
user_name = 'test'
real_wage = 10000  # 每月实际发放的税前标准工资
housing_fund = 1200  # 每月缴纳住房公积金标准金
social_security_amount = 500  # 每月缴纳社保标准金额
wage_exemption = 5000  # 个税免除额标准5000
additional_deduction = 2000  # 每月专项扣除额度合计
annual_bonus = 20000  # 年终奖金额


# 导入数据方式二：命令行输入
# user_name = input("请输入您的姓名或昵称")
# #standard_wage = input("请输入您用于计算公积金、社保的标准工资")
# real_wage = input("请输入您每月实际发放的税前标准工资")
# housing_fund = input("请输入您每月缴纳住房公积金标准金额")
# social_security_amount =input("请输入您每月缴纳社保标准金额")
# wage_exemption = input("请输入您的个税免除额标准") # 5000
# additional_deduction = input("请输入您每月专项扣除额度合计")
# annual_bonus = input("请输入您年终奖金额")


# 计算综合征税税率函数
def individual_tax_rate_function(annual_taxable_wages_total):
    """接收全年应税收入，计算出个税税率及相应的速算扣除数
    :param annual_taxable_wages_total :年度应税工资总额
    :type annual_taxable_wages_total: int 整型或浮点型
    :return individual_tax_rate :个人所得税税率
    :return quick_calculation_deduction:速算扣除数
    """
    if 0 <= annual_taxable_wages_total <= 36000:
        individual_tax_rate = 0.03
        quick_calculation_deduction = 0
        return individual_tax_rate, quick_calculation_deduction

    elif 36000 < annual_taxable_wages_total <= 144000:
        individual_tax_rate = 0.10
        quick_calculation_deduction = 210 * 12
        return individual_tax_rate, quick_calculation_deduction


    elif 144000 < annual_taxable_wages_total <= 300000:
        individual_tax_rate = 0.20
        quick_calculation_deduction = 1410 * 12
        return individual_tax_rate, quick_calculation_deduction


    elif 300000 < annual_taxable_wages_total <= 420000:
        individual_tax_rate = 0.25
        quick_calculation_deduction = 2660 * 12
        return individual_tax_rate, quick_calculation_deduction


    elif 420000 < annual_taxable_wages_total <= 660000:
        individual_tax_rate = 0.30
        quick_calculation_deduction = 4410 * 12
        return individual_tax_rate, quick_calculation_deduction


    elif 660000 < annual_taxable_wages_total <= 960000:
        individual_tax_rate = 0.35
        quick_calculation_deduction = 7160 * 12
        return individual_tax_rate, quick_calculation_deduction


    elif annual_taxable_wages_total > 960000:
        individual_tax_rate = 0.45
        quick_calculation_deduction = 15160 * 12
        return individual_tax_rate, quick_calculation_deduction


# 计算全年一次性奖金税率函数
def one_time_annual_bonus_tax_rate_function(annual_bonus):
    """接收全年应税收入，计算出个税税率及相应的速算扣除数
    :param annual_bonus :全年一次性奖金额度
    :type annual_bonus: int 整型或浮点型
    :return individual_tax_rate :个人所得税税率
    :return quick_calculation_deduction:速算扣除数
    """
    if 0 <= annual_bonus <= 36000:
        individual_tax_rate = 0.03
        quick_calculation_deduction = 0
        return individual_tax_rate, quick_calculation_deduction

    elif 36000 < annual_bonus <= 144000:
        individual_tax_rate = 0.10
        quick_calculation_deduction = 210
        return individual_tax_rate, quick_calculation_deduction


    elif 144000 < annual_bonus <= 300000:
        individual_tax_rate = 0.20
        quick_calculation_deduction = 1410
        return individual_tax_rate, quick_calculation_deduction


    elif 300000 < annual_bonus <= 420000:
        individual_tax_rate = 0.25
        quick_calculation_deduction = 2660
        return individual_tax_rate, quick_calculation_deduction


    elif 420000 < annual_bonus <= 660000:
        individual_tax_rate = 0.30
        quick_calculation_deduction = 4410
        return individual_tax_rate, quick_calculation_deduction


    elif 660000 < annual_bonus <= 960000:
        individual_tax_rate = 0.35
        quick_calculation_deduction = 7160
        return individual_tax_rate, quick_calculation_deduction


    elif annual_bonus > 960000:
        individual_tax_rate = 0.45
        quick_calculation_deduction = 15160
        return individual_tax_rate, quick_calculation_deduction


# 计算进入下一趟税率的应税工资额度
def taxable_wage_quota_function(annual_taxable_wages_total):
    """接收全年应税收入，计算出个税税率及相应的速算扣除数
    :param annual_taxable_wages_total :年度应税工资总额
    :type annual_taxable_wages_total: int 整型或浮点型
    :return individual_tax_rate :个人所得税税率
    :return quick_calculation_deduction:速算扣除数
    """
    if 0 <= annual_taxable_wages_total <= 36000:
        individual_tax_rate = 0.03
        quick_calculation_deduction = 0
        annual_taxable_wages_quota = 36000 * 0.95 - annual_taxable_wages_total
        return individual_tax_rate, quick_calculation_deduction, annual_taxable_wages_quota

    elif 36000 < annual_taxable_wages_total <= 144000:
        individual_tax_rate = 0.10
        quick_calculation_deduction = 210 * 12
        annual_taxable_wages_quota = 144000 * 0.95 - annual_taxable_wages_total
        return individual_tax_rate, quick_calculation_deduction, annual_taxable_wages_quota


    elif 144000 < annual_taxable_wages_total <= 300000:
        individual_tax_rate = 0.20
        quick_calculation_deduction = 1410 * 12
        annual_taxable_wages_quota = 300000 * 0.95 - annual_taxable_wages_total
        return individual_tax_rate, quick_calculation_deduction, annual_taxable_wages_quota


    elif 300000 < annual_taxable_wages_total <= 420000:
        individual_tax_rate = 0.25
        quick_calculation_deduction = 2660 * 12
        annual_taxable_wages_quota = 420000 * 0.95 - annual_taxable_wages_total
        return individual_tax_rate, quick_calculation_deduction, annual_taxable_wages_quota


    elif 420000 < annual_taxable_wages_total <= 660000:
        individual_tax_rate = 0.30
        quick_calculation_deduction = 4410 * 12
        annual_taxable_wages_quota = 660000 * 0.95 - annual_taxable_wages_total
        return individual_tax_rate, quick_calculation_deduction, annual_taxable_wages_quota


    elif 660000 < annual_taxable_wages_total <= 960000:
        individual_tax_rate = 0.35
        quick_calculation_deduction = 7160 * 12
        annual_taxable_wages_quota = 960000 * 0.95 - annual_taxable_wages_total
        return individual_tax_rate, quick_calculation_deduction, annual_taxable_wages_quota


    elif annual_taxable_wages_total > 960000:
        individual_tax_rate = 0.45
        quick_calculation_deduction = 15160 * 12
        annual_taxable_wages_quota = 10000000 - annual_taxable_wages_total
        return individual_tax_rate, quick_calculation_deduction, annual_taxable_wages_quota


"""
方法一：全额综合征税
"""
# 统计所需数据
annual_wage_total1 = real_wage * 12 + annual_bonus  # 全年税前收入
annual_wage_exemption_total = (housing_fund + social_security_amount + wage_exemption + additional_deduction) * 12  # 全年个税免除额
annual_taxable_wages_total1 = annual_wage_total1 - annual_wage_exemption_total  # 全年应税收入
print('\n\n', user_name, '第一种算法测算出，您的：',
      '\n全年税前收入：', annual_wage_total1,
      '\n全年个税免除额:', int(annual_wage_exemption_total),
      '\n全年应税收入：', int(annual_taxable_wages_total1)
      )
# 计算纳税额度
if annual_taxable_wages_total1 > 0:
    individual_tax_rate1 = individual_tax_rate_function(annual_taxable_wages_total1)[0]
    quick_calculation_deduction1 = individual_tax_rate_function(annual_taxable_wages_total1)[1]
else:
    individual_tax_rate1 = 0
    quick_calculation_deduction1 = 0
annual_tax_payment1 = annual_taxable_wages_total1 * individual_tax_rate1 - quick_calculation_deduction1
annual_after_tax_income1 = annual_wage_total1 - annual_tax_payment1 - (housing_fund + social_security_amount) * 12
print('\n年度综合税率为：%0.0f%%' % (individual_tax_rate1 * 100),
      '\n税率速算扣除数为：', quick_calculation_deduction1,
      '\n\n全年纳税额为：', int(annual_tax_payment1),
      '\n全年税后收入：', int(annual_after_tax_income1),
      '\n全年税后收入(含公积金)：', int(annual_after_tax_income1 + housing_fund * 24)
      )

"""
方法二：工资按照全额综合征税计算个税，奖金按照全年一次性奖金计算个税
"""
# 统计工资部分数据
annual_wage_total2 = real_wage * 12  # 全年税前工资收入
annual_taxable_wages_total2 = annual_wage_total2 - annual_wage_exemption_total  # 全年应税收入
print('\n\n', user_name, '第二种算法测算出，您的：',
      '\n全年税前工资：', annual_wage_total2,
      '\n年终奖税前金额为：', annual_bonus,
      '\n全年个税免除额:', int(annual_wage_exemption_total),
      '\n全年应税工资：', int(annual_taxable_wages_total2)
      )
# 计算工资部分纳税额度
if annual_taxable_wages_total2 > 0:
    individual_tax_rate2_1 = individual_tax_rate_function(annual_taxable_wages_total2)[0]
    quick_calculation_deduction2_1 = individual_tax_rate_function(annual_taxable_wages_total2)[1]
else:
    individual_tax_rate2_1 = 0
    quick_calculation_deduction2_1 = 0
annual_tax_payment2_1 = annual_taxable_wages_total2 * individual_tax_rate2_1 - quick_calculation_deduction2_1
annual_after_tax_income2_1 = annual_wage_total2 - annual_tax_payment2_1 - (housing_fund + social_security_amount) * 12

print('\n年度工资部分综合税率为：%0.0f%%' % (individual_tax_rate2_1 * 100),
      '\n工资综合税率速算扣除数为：', quick_calculation_deduction2_1,
      '\n全年工资纳税额为：', int(annual_tax_payment2_1),
      '\n全年税后工资为：', int(annual_after_tax_income2_1),
      )
# 计算年终奖部分纳税额度
individual_tax_rate2_2 = one_time_annual_bonus_tax_rate_function(annual_bonus)[0]
quick_calculation_deduction2_2 = one_time_annual_bonus_tax_rate_function(annual_bonus)[1]
annual_tax_payment2_2 = annual_bonus * individual_tax_rate2_2 - quick_calculation_deduction2_2
annual_after_tax_income2_2 = annual_bonus - annual_tax_payment2_2
annual_tax_payment2 = annual_tax_payment2_1 + annual_tax_payment2_2
annual_after_tax_income2 = annual_after_tax_income2_1 + annual_after_tax_income2_2
print('\n年终奖部分综合税率为：%0.0f%%' % (individual_tax_rate2_2 * 100),
      '\n年终奖税率速算扣除数为：', quick_calculation_deduction2_2,
      '\n年终奖纳税额为：', int(annual_tax_payment2_2),
      '\n年终奖税后为：', int(annual_after_tax_income2_2),
      '\n\n全年纳税额为：', int(annual_tax_payment2),
      '\n全年税后收入：', int(annual_after_tax_income2),
      '\n全年税后收入(含公积金)：', int(annual_after_tax_income2 + housing_fund * 24)
      )

"""
方法三：部分奖金并入工资按照全额综合征税计算个税，剩余奖金按照全年一次性奖金计算个税
"""
# 计算应纳入工资合并计税的奖金额度
if (annual_taxable_wages_total2 + annual_bonus) > 0 and annual_bonus <= 36000:
    annual_bonus3 = 0
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2
elif (annual_taxable_wages_total2 + annual_bonus) > 0 and (36000 < annual_bonus <= 144000):
    annual_bonus3 = 36000
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2 - 36000
elif (annual_taxable_wages_total2 + annual_bonus) > 0 and (144000 < annual_bonus <= 300000):
    annual_bonus3 = 144000
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2 - 144000
elif (annual_taxable_wages_total2 + annual_bonus) > 0 and (300000 < annual_bonus <= 420000):
    annual_bonus3 = 300000
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2 - 300000
elif (annual_taxable_wages_total2 + annual_bonus) > 0 and (420000 < annual_bonus <= 600000):
    annual_bonus3 = 420000
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2 - 420000
elif (annual_taxable_wages_total2 + annual_bonus) > 0 and (600000 < annual_bonus <= 960000):
    annual_bonus3 = 600000
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2 - 600000
elif (annual_taxable_wages_total2 + annual_bonus) > 0 and (960000 < annual_bonus):
    annual_bonus3 = 960000
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2 - 960000
else:
    annual_bonus3 = 0
    taxable_wage_quota = annual_bonus + annual_taxable_wages_total2
annual_wage_total3 = taxable_wage_quota + annual_wage_exemption_total # 全年税前工资收入
annual_taxable_wages_total3 = taxable_wage_quota  # 全年应税收入
print('\n\n', user_name, '第三种算法测算出，您的：',
      '\n全年税前工资及并入年终奖部分税前总额为：', int(annual_wage_total3),
      '\n按照全年一次性奖金计算的年终奖税前金额为：', int(annual_bonus3),
      '\n全年个税免除额:', int(annual_wage_exemption_total),
      '\n全年应税工资：', int(annual_taxable_wages_total3)
      )
# 计算工资部分纳税额度
if annual_taxable_wages_total3 > 0:
    individual_tax_rate3_1 = individual_tax_rate_function(annual_taxable_wages_total3)[0]
    quick_calculation_deduction3_1 = individual_tax_rate_function(annual_taxable_wages_total3)[1]
else:
    individual_tax_rate3_1 = 0
    quick_calculation_deduction3_1 = 0
annual_tax_payment3_1 = annual_taxable_wages_total3 * individual_tax_rate3_1 - quick_calculation_deduction3_1
annual_after_tax_income3_1 = annual_wage_total3 - annual_tax_payment3_1 - (housing_fund + social_security_amount) * 12

print('\n年度工资部分综合税率为：%0.0f%%' % (individual_tax_rate3_1 * 100),
      '\n工资综合税率速算扣除数为：', quick_calculation_deduction3_1,
      '\n全年工资纳税额为：', int(annual_tax_payment3_1),
      '\n全年税后工资为：', int(annual_after_tax_income3_1),
      )
# 计算年终奖部分纳税额度
if annual_bonus3 > 0:
    individual_tax_rate3_2 = one_time_annual_bonus_tax_rate_function(annual_bonus3)[0]
    quick_calculation_deduction3_2 = one_time_annual_bonus_tax_rate_function(annual_bonus3)[1]
    annual_tax_payment3_2 = annual_bonus3 * individual_tax_rate3_2 - quick_calculation_deduction3_2
    annual_after_tax_income3_2 = annual_bonus3 - annual_tax_payment3_2
else:
    individual_tax_rate3_2 = 0
    quick_calculation_deduction3_2 = 0
    annual_tax_payment3_2 = 0
    annual_after_tax_income3_2 = 0
annual_tax_payment3 = annual_tax_payment3_1 + annual_tax_payment3_2
annual_after_tax_income3 = annual_after_tax_income3_1 + annual_after_tax_income3_2
print('\n年终奖部分综合税率为：%0.0f%%' % (individual_tax_rate3_2 * 100),
      '\n年终奖税率速算扣除数为：', quick_calculation_deduction3_2,
      '\n年终奖纳税额为：', int(annual_tax_payment3_2),
      '\n年终奖税后为：', int(annual_after_tax_income3_2),
      '\n\n全年纳税额为：', int(annual_tax_payment3),
      '\n全年税后收入：', int(annual_after_tax_income3),
      '\n全年税后收入(含公积金)：', int(annual_after_tax_income3 + housing_fund * 24)
      )

# 判断那套方案更合算
if annual_after_tax_income1 >= annual_after_tax_income2 and annual_after_tax_income1 >= annual_after_tax_income3:
    print('\n\n第一种算法更合理:',
          '\n全年纳税额为：', int(annual_tax_payment1),
          '\n全年税后收入：', int(annual_after_tax_income1),
          '\n全年税后收入(含公积金)：', int(annual_after_tax_income1 + housing_fund * 24)
          )
elif annual_after_tax_income2 >= annual_after_tax_income1 and annual_after_tax_income2 >= annual_after_tax_income3:
    print('\n\n第二种算法更合理:',
          '\n全年纳税额为：', int(annual_tax_payment2),
          '\n全年税后收入：', int(annual_after_tax_income2),
          '\n全年税后收入(含公积金)：', int(annual_after_tax_income2 + housing_fund * 24)
          )
elif annual_after_tax_income3 >= annual_after_tax_income1 and annual_after_tax_income3 >= annual_after_tax_income2:
    print('\n\n第三种算法更合理:',
          '\n全年纳税额为：', int(annual_tax_payment3),
          '\n全年税后收入：', int(annual_after_tax_income3),
          '\n全年税后收入(含公积金)：', int(annual_after_tax_income3 + housing_fund * 24)
          )
print('计算耗时：', (time.clock() - start_time))
