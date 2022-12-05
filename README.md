# final-pjt

- 팀명

  - TOPTEN

- 팀원

  - 이동우
    - Main Task
    - BE
    - Sub Task
    - FE
  - 이성훈
    - Main Task
    - FE
    - Sub Task
    - UX/UI

- 목표 서비스

  - 전체 영화
    - 검색기능과 장르별 영화 기능
  - 유저
    - 멀티 프로필
    - 프로필별 TOP 10 영화 선택 및 좋아요, 위시리스트 기능
    - 프로필 페이지를 개인 정보와 TOP 10 수정 기능
  - 개별 영화
    - 영화 정보
    - 배우, 감독, 포스터, 트레일러영상, 연관된 영화 등
    - 코멘트
  - 본인과 비슷한 취향의 유저 추천
    - TOP10, 좋아요, 위시리스트를 통한 추천

- 데이터 베이스 모델링 (ERD)

  - [ERD](https://www.erdcloud.com/d/uSc6zDDhNZKH9s55v)

- 컴포넌트 모델링

  - `컴포넌트.drawio` 파일로 업로드

- 추천 알고리즘

  - TOPTEN으로 선택한 영화를 기반으로 취향이 비슷한 상대방을 추천
  - 먼저 1위 영화에 대한 선호가 있는 유저를 filter
  - 이후 2위, 3위 등 후순위에 대한 영화에 대한 선호도 있는지도 계속하여 filter
  - 가장 취향이 비슷한 유저는 본인이기에 본인은 제외해야 함
  - 본인을 제외한 비슷한 유저중 랜덩으로 한 유저의 프로필 페이지로 매칭

- 배포 서버 URL

  - 조금 더 손 본뒤 배포 예정...

- 느낀점

  - 라이브러리 사용
    - 라이브러리를 활용할 시간이 없다고 판단하여 최소한 사용
    - 하지만 사용하는 것이 공부도 되고 나중을 위해 훨씬 좋았을 것이라 생각...
  - auth(account, user)
    - 메일을 이용한 로그인 및 메일 인증을 통한 로그인을 구현하고자 했지만 실패함
    - 나중을 위해 일부러 User모델을 손대지 않았지만 현재도 손대지 않은채임
    - 중간에 JWT 토큰을 잠깐 사용하였는데 이에 대한 이해가 많이 부족함
    - 새로고침하여도 로그인이 유지되도록 하려 했지만 역시 시간 부족
  - re-rendering
    - vue가 rendering되는 경우가 정확히 언제인지 아직도 모르겠음
    - 자신, 부모, 자식 컴포넌트를 아무리 감지해도 안되는 경우가 있음
  - serializer
    - serialize하고 싶지만 ERD 구조상 접근이 까다로운 경우가 생각보다 많았음
    - 조금만 더 잘 사용하면 axios 사용을 반은 줄일 수 있지 않았을까

- 마지막 할 말
  - 공부와 실전은 너무 다르다...
  - 정말 시간이 아쉬웠다는 생각 뿐입니다....
  - 사실상 벌써 6시라 README를 작성할 시간도 없습니다.....ㄴㅇ
