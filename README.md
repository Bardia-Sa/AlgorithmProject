``` mermaid
  graph LR
    A((شروع برنامه)) --> B[تعریف متغیرها و پارامترها]
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
    L --> M[محاسبه مقدار تحلیلی و خطا]
    M --> E
    E -- خیر --> N[نمایش نتایج]
    N --> O((پایان برنامه))
    
    subgraph "تعریف متغیرها و پارامترها"
        B1[t_start, t_end, h, t, y1, y2, k1-k4, m1-m4, y1_analytic, error, n, i]
        B2[آرایه‌های t_values, y1_values, y2_values, y_analytic_values, error_values]
        B --> B1
        B --> B2
    end
    
    subgraph "تعریف تابع f(t, y1, y2)"
        C1[f_val(1) = y2]
        C2[f_val(2) = 3*y2 - 2*y1 + 6*exp(-t)]
        C --> C1
        C --> C2
    end
    
    subgraph "مقداردهی اولیه"
         D1[y1 = 2, y2 = 2, t = t_start]
         D2[ذخیره مقادیر اولیه در آرایه ها]
         D3[محاسبه مقدار تحلیلی در t=0]
         D --> D1
         D --> D2
         D --> D3
    end

    subgraph "محاسبه k1 و m1"
      F1[f_val = f(t, y1, y2)]
      F2[k1 = f_val(1), m1 = f_val(2)]
      F --> F1
      F --> F2
    end

    subgraph "محاسبه k2 و m2"
      G1[f_val = f(t + h/2, y1 + k1*h/2, y2 + m1*h/2)]
      G2[k2 = f_val(1), m2 = f_val(2)]
      G --> G1
      G --> G2
    end

    subgraph "محاسبه k3 و m3"
      H1[f_val = f(t + h/2, y1 + k2*h/2, y2 + m2*h/2)]
      H2[k3 = f_val(1), m3 = f_val(2)]
      H --> H1
      H --> H2
    end
    
    subgraph "محاسبه k4 و m4"
      I1[f_val = f(t + h, y1 + k3*h, y2 + m3*h)]
      I2[k4 = f_val(1), m4 = f_val(2)]
       I --> I1
      I --> I2
    end
    
    subgraph "بروزرسانی y1 و y2"
      J1[y1 = y1 + (h/6) * (k1 + 2*k2 + 2*k3 + k4)]
      J2[y2 = y2 + (h/6) * (m1 + 2*m2 + 2*m3 + m4)]
      J --> J1
      J --> J2
   end

   subgraph "بروزرسانی زمان (t = t + h)"
         K1[t = t+h]
        K --> K1
   end

   subgraph "ذخیره مقادیر در آرایه ها"
        L1[ذخیره t, y1, y2 در آرایه‌ها]
        L --> L1
    end

    subgraph "محاسبه مقدار تحلیلی و خطا"
        M1[محاسبه مقدار تحلیلی]
        M2[محاسبه خطا]
        M --> M1
        M --> M2
    end
    
    subgraph "نمایش نتایج"
       N1[چاپ مقادیر t, y1, y1_analytic, error در هر گام]
        N2[محاسبه و چاپ حداکثر خطا]
        N --> N1
        N --> N2
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style O fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ffc,stroke:#333,stroke-width:2px
    style N fill:#aaf,stroke:#333,stroke-width:2px
```
