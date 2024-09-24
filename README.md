# ABO

해당 프로그램은 K-shield.Jr 내 ABO 팀의 프로젝트를 위해 만들어졌습니다.<br>
오타스쿼팅공격을 겨냥한 패키지의 다운을 사전에 방지하기 위해 이름의 유사도를 계산하여 오타스쿼팅의 가능성이 있는지를 판독합니다.<br>
판독 결과를 통해 사용자가 잘못된 패키지를 다운받으려 함을 알리며, 해당 패키지와 유사한 이름을 가진 상위 3개의 패키지 목록을 출력합니다.<br>
사용자는 패키지를 해당 목록 혹은 입력한 패키지를 다운받거나 다운받지 않을 수 있습니다.<br><br>

오타 스쿼팅 판별 기준
-------------
기존 패키지와 입력한 패키지명의 유사도를 계산하여, 유사도를 기준으로 판별합니다.<br>
<table>
  <tr>
    <th> 유사도 </th>
    <th> 판별 결과 </th>
  </tr>
  <tr>
    <th> 유사도 = 1 </th>
    <th> 정상 패키지 </th>
  </tr>
  <tr>
    <th> 유사도 >= 0.9 </th>
    <th> 오타스쿼팅 겨냥 패키지 </th>
  </tr>
  <tr>
    <th> 유사도 < 0.9 </th>
    <th> 사용자 제작 패키지 </th>
  </tr>
</table>


정상 패키지 명 데이터셋
-------------

debian.org 에서 패키지명 72,679개 수집 후 이를 유사도 판별 기준 데이터셋으로 사용


개발 및 사용환경
-------------
해당 프로젝트는 데비안 계열의 운영체제에서 제작되어 해당 계열의 운영체제에서의 사용을 지원합니다.<br>
현재 레드헷 계열의 운영체제 계열에서의 사용은 지원되지 않고 있습니다.<br>
다른 운영체제에서는 원활히 동작하지 않을 수 있습니다.
