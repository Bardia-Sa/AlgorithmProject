graph LR
    A((شروع)) --> B[تعریف متغیرها و پارامترها]
    B --> C[تعریف تابع f(t, y1, y2)]
    C --> D[مقداردهی اولیه]
    D --> E{حلقه اصلی (i=1 to n)}
    E -- بله --> F[محاسبه k1 و m1]
    F --> G[محاسبه k2 و m2]
    G --> H[محاسبه k3 و m3]
    H --> I[محاسبه k4 و m4]
    I --> J[بروزرسانی y1 و y2]
    J --> K[بروزرسانی زمان (t = t + h)]
    K --> L[ذخیره مقادیر در آرایه ها]
    L --> M{محاسبه y_analytic؟}
    M -- بله --> N[محاسبه مقدار تحلیلی y_analytic]
    N --> O[محاسبه خطا (error = |y1 - y_analytic|)]
    O --> E
    M -- خیر --> E
    E -- خیر --> P[نمایش نتایج]
    P --> Q((پایان))
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style Q fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:1px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ffc,stroke:#333,stroke-width:2px
    style P fill:#aaf,stroke:#333,stroke-width:2px
