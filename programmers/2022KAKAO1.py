def solution(id_list, report, k):
  answer = []
  report_me_user_list = {}
  mail_list = {}

  for id in id_list:
      report_me_user_list[id] = []
      mail_list[id] = 0

  for report in report:
      report_me_user_list[report.split(" ")[1]].append(report.split(" ")[0])

  for key, value in report_me_user_list.items():
      report_me_user_list[key] = list(set(value))
      if(len(report_me_user_list[key]) >= k):
          for mail in report_me_user_list[key]:
              mail_list[mail] += 1

  for mail in mail_list.values():
      answer.append(mail)

  return answer