``` mermaid
  graph LR
    A((شروع)) --> B[تعریف متغیرها و پارامترها] --> C[تعریف تابع f(t, y1, y2)] --> D[مقداردهی اولیه] --> E{حلقه اصلی (i=1 to n)}
    E -- بله --> F[محاسبه k1 و m1] --> G[محاسبه k2 و m2] --> H[محاسبه k3 و m3] --> I[محاسبه k4 و m4] --> J[بروزرسانی y1 و y2] --> K[بروزرسانی زمان (t = t + h)] --> L[ذخیره مقادیر در آرایه ها] --> M{محاسبه y_analytic؟}
    M -- بله --> N[محاسبه مقدار تحلیلی y_analytic] --> O[محاسبه خطا (error = |y1 - y_analytic|)] --> E
    M -- خیر --> E
    E -- خیر --> P[نمایش نتایج] --> Q((پایان))
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style Q fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:1px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ffc,stroke:#333,stroke-width:2px
    style P fill:#aaf,stroke:#333,stroke-width:2px


```
