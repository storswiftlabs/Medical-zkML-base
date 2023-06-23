program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
		p7: u32,
		p8: u32,
		p9: u32,
		p10: u32,
		p11: u32,
		p12: u32,
		p13: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p13 < 45u32) {
			if (inputs.p12 < 5u32) {
				if (inputs.p1 < 575u32) {
					if (inputs.p10 < 36u32) {
						if (inputs.p4 <= 1090u32) {
							if (inputs.p4 <= 1060u32) {
								return 0u32;
							} else {
								if (inputs.p2 < 5u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							}
						} else {
							return 0u32;
						}
					} else {
						return 1u32;
					}
				} else {
					if (inputs.p8 < 835u32) {
						return 2u32;
					} else {
						if (inputs.p1 < 645u32) {
							if (inputs.p6 < 5u32) {
								if (inputs.p8 < 1705u32) {
									if (inputs.p4 <= 1150u32) {
										return 0u32;
									} else {
										if (inputs.p3 < 35u32) {
											return 1u32;
										} else {
											if (inputs.p10 < 4u32) {
												if (inputs.p11 < 15u32) {
													if (inputs.p8 <= 1660u32) {
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
										}
									}
								} else {
									return 0u32;
								}
							} else {
								return 0u32;
							}
						} else {
							return 0u32;
						}
					}
				}
			} else {
				if (inputs.p3 < 35u32) {
					if (inputs.p5 < 2375u32) {
						if (inputs.p5 < 2225u32) {
							if (inputs.p12 < 15u32) {
								return 0u32;
							} else {
								if (inputs.p2 < 5u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							}
						} else {
							if (inputs.p12 < 15u32) {
								return 1u32;
							} else {
								return 2u32;
							}
						}
					} else {
						return 0u32;
					}
				} else {
					if (inputs.p2 < 5u32) {
						if (inputs.p4 <= 1340u32) {
							return 0u32;
						} else {
							if (inputs.p4 <= 1390u32) {
								return 2u32;
							} else {
								return 3u32;
							}
						}
					} else {
						if (inputs.p1 <= 530u32) {
							if (inputs.p5 < 2825u32) {
								return 1u32;
							} else {
								return 2u32;
							}
						} else {
							if (inputs.p4 < 1235u32) {
								if (inputs.p11 < 15u32) {
									return 2u32;
								} else {
									return 3u32;
								}
							} else {
								if (inputs.p4 <= 1490u32) {
									if (inputs.p10 < 7u32) {
										return 4u32;
									} else {
										if (inputs.p5 < 2075u32) {
											return 4u32;
										} else {
											return 1u32;
										}
									}
								} else {
									return 2u32;
								}
							}
						}
					}
				}
			}
		} else {
			if (inputs.p10 < 9u32) {
				if (inputs.p7 <= 10u32) {
					if (inputs.p12 < 5u32) {
						if (inputs.p8 < 1275u32) {
							return 1u32;
						} else {
							if (inputs.p5 < 2505u32) {
								return 0u32;
							} else {
								if (inputs.p5 <= 2620u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						}
					} else {
						if (inputs.p1 < 575u32) {
							if (inputs.p6 < 5u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p5 < 2545u32) {
								return 2u32;
							} else {
								return 0u32;
							}
						}
					}
				} else {
					if (inputs.p3 < 35u32) {
						if (inputs.p4 <= 1240u32) {
							return 0u32;
						} else {
							if (inputs.p6 < 5u32) {
								if (inputs.p8 <= 1610u32) {
									return 1u32;
								} else {
									if (inputs.p4 <= 1610u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								}
							} else {
								return 2u32;
							}
						}
					} else {
						if (inputs.p4 <= 1280u32) {
							if (inputs.p11 < 15u32) {
								return 1u32;
							} else {
								return 3u32;
							}
						} else {
							if (inputs.p4 <= 1550u32) {
								if (inputs.p13 < 65u32) {
									return 1u32;
								} else {
									return 3u32;
								}
							} else {
								return 4u32;
							}
						}
					}
				}
			} else {
				if (inputs.p8 <= 1330u32) {
					if (inputs.p8 < 1275u32) {
						if (inputs.p5 < 2825u32) {
							if (inputs.p9 < 5u32) {
								if (inputs.p4 < 1405u32) {
									if (inputs.p5 <= 2720u32) {
										return 2u32;
									} else {
										return 3u32;
									}
								} else {
									if (inputs.p4 <= 1550u32) {
										return 1u32;
									} else {
										return 3u32;
									}
								}
							} else {
								if (inputs.p13 < 65u32) {
									if (inputs.p8 < 1155u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								} else {
									if (inputs.p1 < 635u32) {
										if (inputs.p5 < 2525u32) {
											return 3u32;
										} else {
											if (inputs.p7 <= 10u32) {
												return 3u32;
											} else {
												return 1u32;
											}
										}
									} else {
										if (inputs.p10 < 28u32) {
											return 4u32;
										} else {
											return 3u32;
										}
									}
								}
							}
						} else {
							if (inputs.p9 < 5u32) {
								return 4u32;
							} else {
								return 2u32;
							}
						}
					} else {
						if (inputs.p4 <= 1290u32) {
							if (inputs.p10 < 28u32) {
								return 1u32;
							} else {
								return 3u32;
							}
						} else {
							if (inputs.p10 < 19u32) {
								return 3u32;
							} else {
								return 4u32;
							}
						}
					}
				} else {
					if (inputs.p9 < 5u32) {
						if (inputs.p5 <= 2260u32) {
							if (inputs.p1 < 585u32) {
								return 3u32;
							} else {
								return 2u32;
							}
						} else {
							if (inputs.p3 < 35u32) {
								if (inputs.p5 <= 2300u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p10 < 19u32) {
									return 2u32;
								} else {
									if (inputs.p4 <= 1320u32) {
										return 4u32;
									} else {
										if (inputs.p2 < 5u32) {
											return 3u32;
										} else {
											return 0u32;
										}
									}
								}
							}
						}
					} else {
						if (inputs.p11 < 15u32) {
							if (inputs.p4 < 1235u32) {
								return 2u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p8 < 1525u32) {
								if (inputs.p10 < 12u32) {
									return 1u32;
								} else {
									if (inputs.p1 < 595u32) {
										return 2u32;
									} else {
										if (inputs.p5 <= 2590u32) {
											return 1u32;
										} else {
											return 2u32;
										}
									}
								}
							} else {
								if (inputs.p7 <= 10u32) {
									return 4u32;
								} else {
									return 1u32;
								}
							}
						}
					}
				}
			}
		}
	}
}