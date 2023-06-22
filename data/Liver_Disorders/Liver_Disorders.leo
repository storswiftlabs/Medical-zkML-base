program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p5 < 205u32) {
			if (inputs.p3 < 205u32) {
				if (inputs.p5 < 95u32) {
					if (inputs.p1 <= 830u32) {
						return 1u32;
					} else {
						return 0u32;
					}
				} else {
					if (inputs.p2 < 775u32) {
						if (inputs.p1 < 945u32) {
							if (inputs.p1 < 825u32) {
								if (inputs.p1 < 735u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p1 < 885u32) {
									return 1u32;
								} else {
									if (inputs.p3 < 125u32) {
										return 1u32;
									} else {
										if (inputs.p2 <= 560u32) {
											if (inputs.p2 < 485u32) {
												return 1u32;
											} else {
												return 0u32;
											}
										} else {
											if (inputs.p4 <= 150u32) {
												return 0u32;
											} else {
												return 1u32;
											}
										}
									}
								}
							}
						} else {
							if (inputs.p1 <= 970u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					} else {
						if (inputs.p1 < 895u32) {
							return 1u32;
						} else {
							if (inputs.p2 <= 1250u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					}
				}
			} else {
				if (inputs.p1 < 875u32) {
					if (inputs.p3 < 265u32) {
						if (inputs.p2 <= 720u32) {
							if (inputs.p5 < 175u32) {
								return 1u32;
							} else {
								if (inputs.p4 < 145u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						} else {
							return 0u32;
						}
					} else {
						return 0u32;
					}
				} else {
					if (inputs.p4 <= 210u32) {
						if (inputs.p1 < 945u32) {
							return 0u32;
						} else {
							if (inputs.p5 <= 170u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					} else {
						if (inputs.p4 < 225u32) {
							if (inputs.p1 <= 920u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p3 < 375u32) {
								return 0u32;
							} else {
								if (inputs.p5 <= 180u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						}
					}
				}
			}
		} else {
			if (inputs.p6 < 55u32) {
				if (inputs.p2 < 655u32) {
					if (inputs.p1 < 895u32) {
						return 1u32;
					} else {
						if (inputs.p1 < 915u32) {
							if (inputs.p2 <= 480u32) {
								return 1u32;
							} else {
								if (inputs.p3 <= 380u32) {
									if (inputs.p6 < 35u32) {
										if (inputs.p5 < 255u32) {
											return 1u32;
										} else {
											return 0u32;
										}
									} else {
										return 1u32;
									}
								} else {
									return 1u32;
								}
							}
						} else {
							if (inputs.p1 < 975u32) {
								return 1u32;
							} else {
								if (inputs.p3 <= 300u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						}
					}
				} else {
					if (inputs.p4 < 225u32) {
						if (inputs.p6 < 35u32) {
							if (inputs.p3 <= 360u32) {
								if (inputs.p5 <= 800u32) {
									if (inputs.p4 < 215u32) {
										if (inputs.p1 < 955u32) {
											if (inputs.p3 < 185u32) {
												if (inputs.p6 < 13u32) {
													return 1u32;
												} else {
													return 0u32;
												}
											} else {
												return 0u32;
											}
										} else {
											return 1u32;
										}
									} else {
										return 1u32;
									}
								} else {
									if (inputs.p4 < 205u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								}
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p2 <= 680u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					} else {
						if (inputs.p3 <= 360u32) {
							return 1u32;
						} else {
							if (inputs.p4 <= 350u32) {
								if (inputs.p4 <= 300u32) {
									if (inputs.p4 < 265u32) {
										if (inputs.p1 <= 920u32) {
											return 0u32;
										} else {
											return 1u32;
										}
									} else {
										return 1u32;
									}
								} else {
									return 0u32;
								}
							} else {
								return 1u32;
							}
						}
					}
				}
			} else {
				if (inputs.p1 < 915u32) {
					if (inputs.p4 < 215u32) {
						return 0u32;
					} else {
						if (inputs.p5 <= 250u32) {
							if (inputs.p2 < 585u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							return 1u32;
						}
					}
				} else {
					if (inputs.p5 < 365u32) {
						return 0u32;
					} else {
						if (inputs.p2 <= 720u32) {
							if (inputs.p1 < 975u32) {
								if (inputs.p5 < 1475u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							} else {
								if (inputs.p4 <= 400u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						} else {
							if (inputs.p6 <= 140u32) {
								if (inputs.p5 <= 750u32) {
									if (inputs.p1 <= 980u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								} else {
									if (inputs.p5 < 1615u32) {
										if (inputs.p6 < 105u32) {
											return 0u32;
										} else {
											return 1u32;
										}
									} else {
										return 1u32;
									}
								}
							} else {
								return 0u32;
							}
						}
					}
				}
			}
		}
	}
}