# Understanding Host Network Stack Overheads

This project analyzes and reproduces the results from the paper "Understanding Host Network Stack Overheads" (SIGCOMM 2021), and extends the evaluation with additional scenarios.

## Report Structure

The report includes:

1. **Introduction**: Background on network stack performance and overview of the original paper
2. **Background and Related Work**: Overview of network stack architecture, hardware offloads, and related research
3. **Methodology of the Original Paper**: Detailed description of the hardware configuration, kernel modifications, experimental scenarios, and performance metrics used in the original paper
4. **Analysis of Original Results**: Comprehensive analysis of the results presented in the original paper, including single flow performance, multi-flow scenarios, and special scenarios
5. **Proposed Extended Evaluation**: Detailed designs for extending the evaluation beyond the original paper, including the impact of CPU frequency scaling, interrupt coalescing, application workload patterns, and congestion control algorithms
6. **Discussion**: Synthesis of findings, practical recommendations, and limitations
7. **Conclusion**: Summary of key insights and future work

## Figures

The report includes recreated versions of the key figures from the original paper:

- **Figure 3**: Single flow performance with different optimizations
- **Figure 4**: One-to-one performance with multiple flows
- **Figure 5**: Incast performance with multiple senders to a single receiver
- **Figure 7**: Impact of packet loss on TCP performance
- **Figure 8**: Short flow performance in an incast scenario

It also includes theoretical figures for the proposed extended evaluation:

- **CPU Frequency Impact**: Theoretical impact of CPU frequency on network performance with different optimizations
- **Interrupt Coalescing**: Theoretical trade-off between throughput and latency with different interrupt coalescing settings
- **Workload Patterns**: Theoretical performance characteristics of different application workload patterns
- **Congestion Control**: Theoretical performance of different congestion control algorithms under varying packet loss rates

## References

- Original paper: Q. Cai, S. Chaudhary, M. Vuppalapati, J. Hwang, and R. Agarwal, "Understanding Host Network Stack Overheads," in Proceedings of the 2021 ACM SIGCOMM Conference, 2021, pp. 65–77.
