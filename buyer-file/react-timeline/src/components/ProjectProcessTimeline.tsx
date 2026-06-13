import React from "react";
import { motion } from "framer-motion";
import {
  ClipboardCheck,
  PencilRuler,
  Calculator,
  Settings2,
  FileSpreadsheet,
  FileText,
  Send,
  Scale,
  HardHat,
  CheckCircle,
  LucideIcon
} from "lucide-react";

interface Step {
  id: number;
  title: string;
  description: string;
  icon: LucideIcon;
}

const steps: Step[] = [
  {
    id: 1,
    title: "Building Survey & Feasibility Study",
    description: "Comprehensive site assessment and viability analysis to establish project foundations.",
    icon: ClipboardCheck
  },
  {
    id: 2,
    title: "Concept Design Submittal",
    description: "Design concepts developed based on complete client input and requirements.",
    icon: PencilRuler
  },
  {
    id: 3,
    title: "Budgetary Proposal",
    description: "Cost estimation and financial planning based on approved concept design.",
    icon: Calculator
  },
  {
    id: 4,
    title: "Detail Design Development",
    description: "Engineering-driven detailed design development for all MEPF systems.",
    icon: Settings2
  },
  {
    id: 5,
    title: "Bill of Quantities",
    description: "Preparation of comprehensive BOQ for accurate project costing.",
    icon: FileSpreadsheet
  },
  {
    id: 6,
    title: "Material & Technical Specifications",
    description: "Detailed specifications for materials, equipment, and installation standards.",
    icon: FileText
  },
  {
    id: 7,
    title: "Tender Documents & Floating",
    description: "Preparation of tender documents and release to qualified contractors.",
    icon: Send
  },
  {
    id: 8,
    title: "Vendor Bid Evaluation",
    description: "Review and evaluation of bids to select the right contractor for execution.",
    icon: Scale
  },
  {
    id: 9,
    title: "Construction Documents",
    description: "Contractor-prepared construction drawings and execution plans.",
    icon: HardHat
  },
  {
    id: 10,
    title: "Commissioning & Execution Analysis",
    description: "Pre and post commissioning with performance analysis of installed systems.",
    icon: CheckCircle
  }
];

export default function ProjectProcessTimeline() {
  return (
    <section className="relative w-full bg-[#111111] py-24 px-4 sm:px-6 lg:px-8 overflow-hidden">
      {/* Background patterns */}
      <div className="absolute inset-0 opacity-5 pointer-events-none">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-[#C9F31D] rounded-full blur-3xl" />
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-[#C9F31D] rounded-full blur-3xl" />
      </div>

      <div className="max-w-5xl mx-auto relative z-10">
        {/* Section Header */}
        <div className="flex flex-col items-center text-center mb-20">
          {/* Accent dot matching our featured works */}
          <div className="w-3 h-3 bg-[#C9F31D] rounded-full mb-4 shadow-[0_0_12px_rgba(201,243,29,0.8)]" />
          <h2 className="text-4xl sm:text-5xl font-extrabold text-white tracking-tight">
            Project Process Flow
          </h2>
          <p className="mt-4 text-lg text-neutral-400 max-w-2xl font-light">
            How we deliver excellence from concept to commissioning
          </p>
        </div>

        {/* Timeline Container */}
        <div className="relative flex flex-col items-stretch">
          {/* Main vertical dotted line */}
          <div 
            className="absolute left-[24px] sm:left-[24px] top-6 bottom-6 w-[2px] pointer-events-none"
            style={{
              backgroundImage: "linear-gradient(to bottom, #333333 60%, rgba(255,255,255,0) 0%)",
              backgroundSize: "2px 8px",
              backgroundRepeat: "repeat-y"
            }}
          />

          {/* Steps wrapper */}
          <div className="space-y-12 sm:space-y-16">
            {steps.map((step, index) => {
              const IconComponent = step.icon;

              return (
                <motion.div
                  key={step.id}
                  className="flex items-start gap-6 sm:gap-8 relative"
                  initial="hidden"
                  whileInView="visible"
                  viewport={{ once: false, margin: "-10%" }}
                  variants={{
                    hidden: {},
                    visible: {
                      transition: {
                        staggerChildren: 0.15
                      }
                    }
                  }}
                >
                  {/* Step Connecting Progress Line (fills up on scroll-in) */}
                  {index > 0 && (
                    <motion.div
                      className="absolute left-[24px] w-[2px] bg-[#C9F31D] origin-top"
                      style={{
                        top: `-${index === 1 ? 64 : 48}px`,
                        height: `${index === 1 ? 64 : 48}px`
                      }}
                      variants={{
                        hidden: { scaleY: 0 },
                        visible: { scaleY: 1, transition: { duration: 0.5, ease: "easeOut" } }
                      }}
                    />
                  )}

                  {/* Circle Step Indicator */}
                  <div className="relative flex-shrink-0 z-10">
                    <motion.div
                      className="w-12 h-12 rounded-full border-2 border-neutral-700 bg-neutral-900 flex items-center justify-center text-white"
                      variants={{
                        hidden: { 
                          backgroundColor: "#171717",
                          borderColor: "#404040",
                          color: "#ffffff"
                        },
                        visible: { 
                          backgroundColor: "#C9F31D",
                          borderColor: "#C9F31D",
                          color: "#111111",
                          boxShadow: "0 0 16px rgba(201, 243, 29, 0.4)",
                          transition: { duration: 0.4 }
                        }
                      }}
                    >
                      <IconComponent className="w-5 h-5 flex-shrink-0" />
                    </motion.div>

                    {/* Active pulse effect */}
                    <motion.div
                      className="absolute -inset-1 rounded-full border-2 border-[#C9F31D]/40 pointer-events-none"
                      initial={{ opacity: 0, scale: 0.8 }}
                      variants={{
                        hidden: { opacity: 0, scale: 0.8 },
                        visible: {
                          opacity: [0, 1, 0],
                          scale: [1, 1.25, 1.4],
                          transition: {
                            repeat: Infinity,
                            duration: 2,
                            ease: "easeOut"
                          }
                        }
                      }}
                    />
                  </div>

                  {/* Content Card */}
                  <motion.div
                    className="flex-grow bg-[#1a1a1a] rounded-xl border border-neutral-800 p-6 md:p-8"
                    variants={{
                      hidden: { 
                        opacity: 0, 
                        x: 30,
                        borderLeftColor: "#262626",
                        borderLeftWidth: "3px"
                      },
                      visible: { 
                        opacity: 1, 
                        x: 0,
                        borderLeftColor: "#C9F31D",
                        borderLeftWidth: "3px",
                        transition: { 
                          type: "spring",
                          stiffness: 100,
                          damping: 15
                        }
                      }
                    }}
                  >
                    <span className="text-xs font-bold uppercase tracking-wider text-[#C9F31D]">
                      Step 0{step.id}
                    </span>
                    <h3 className="text-xl sm:text-2xl font-bold text-white mt-1">
                      {step.title}
                    </h3>
                    <p className="mt-2 text-neutral-400 font-light leading-relaxed">
                      {step.description}
                    </p>
                  </motion.div>
                </motion.div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}
